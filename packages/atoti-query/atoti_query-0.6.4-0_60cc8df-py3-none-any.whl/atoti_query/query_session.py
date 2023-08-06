import json
from dataclasses import dataclass, field
from ssl import SSLContext, create_default_context
from typing import Any, Dict, Iterable, Mapping, Optional, Union, cast
from urllib.error import HTTPError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

import pandas as pd
from atoti_core import (
    BaseCondition,
    BaseLevel,
    BaseMeasure,
    BaseSession,
    BaseSessionBound,
    ServerVersions,
    decombine_condition,
    deprecated,
    get_active_plugins,
    get_java_coordinates,
    keyword_only_dataclass,
    local_to_absolute_path,
)
from typing_extensions import Literal

from ._cellset import Cellset
from ._cellset_to_query_result import cellset_to_query_result
from ._context import Context
from ._create_query_cubes_from_discovery import create_query_cubes_from_discovery
from ._discovery import Discovery
from ._execute_arrow_query import execute_arrow_query
from ._get_level_java_types import GetLevelJavaTypes
from ._widget_conversion_details import WidgetConversionDetails
from .auth import Auth
from .client_certificate import ClientCertificate
from .query_cubes import QueryCubes


def _create_ssl_context(client_certificate: ClientCertificate) -> SSLContext:
    context = create_default_context()
    if client_certificate.certificate_authority:
        context.load_verify_locations(
            cafile=local_to_absolute_path(client_certificate.certificate_authority)
        )
    context.load_cert_chain(
        certfile=local_to_absolute_path(client_certificate.certificate),
        keyfile=local_to_absolute_path(client_certificate.keyfile)
        if client_certificate.keyfile
        else None,
        password=client_certificate.password,
    )
    return context


def _serialize_condition(condition: BaseCondition) -> Dict[str, Any]:
    (
        level_conditions,
        level_isin_conditions,
        hierarchy_isin_conditions,
    ) = decombine_condition(condition)

    # Ensure there is no hierarchy conditions
    if hierarchy_isin_conditions:
        raise ValueError("Unsupported hierarchy isin condition in raw query mode.")

    # Ensure all condition are == or isin on strings
    for level_condition in level_conditions:
        if level_condition.operator != "eq":
            raise ValueError(
                f"'{level_condition.operator}' not supported in query condition: level conditions can only be based on equality (==) or isin."
            )
        if not isinstance(level_condition.value, str):
            raise TypeError(
                f"Type {type(level_condition.value)} not supported in query condition: level conditions can only be based on equality with strings."
            )
    for level_isin_condition in level_isin_conditions:
        not_string = [
            value
            for value in level_isin_condition.members
            if not isinstance(value, str)
        ]
        if not_string:
            raise TypeError(
                f"Only strings are supported in query condition but the following values are not strings: {str(not_string)}."
            )

    # Serialize the conditions
    equal_conditions = {
        get_java_coordinates(level_condition.level_coordinates): level_condition.value
        for level_condition in level_conditions
    }
    isin_conditions = {
        get_java_coordinates(level_condition.level_coordinates): level_condition.members
        for level_condition in level_isin_conditions
    }
    return {
        "equalConditions": equal_conditions,
        "isinConditions": isin_conditions,
    }


@keyword_only_dataclass
@dataclass(frozen=True)
class _QuerySessionPrivateParameters:
    server_versions: Optional[ServerVersions] = None


@keyword_only_dataclass
@dataclass(frozen=True)
class _QueryMdxPrivateParameters:
    session: Optional[BaseSessionBound] = None
    get_level_java_types: Optional[GetLevelJavaTypes] = None
    context: Context = field(default_factory=dict)


class QuerySession(BaseSession[QueryCubes]):
    """Used to query a remote atoti session (or a classic ActivePivot >= 5.7 server).

    Args:
        url: The base URL of the session.
            The endpoint ``f"{url}/versions/rest"`` is expected to exist.
        auth: The authentication to use to access the session.
        client_certificate: The client certificate to authenticate against the session.

    Note:
        Query sessions are immutable: the structure of their underlying cubes is not expected to change.
    """

    __cubes: Optional[QueryCubes] = None
    __discovery: Optional[Discovery] = None
    __ssl_context: Optional[SSLContext] = None

    def __init__(
        self,
        url: str,
        *,
        auth: Optional[Auth] = None,
        client_certificate: Optional[ClientCertificate] = None,
        name: Optional[str] = None,
        **kwargs: Any,
    ):
        if name is not None:
            deprecated("Naming a query session is deprecated.")

        super().__init__()
        self._url = url
        self._name = name or url
        self._auth = auth or (lambda _: None)
        self._client_certificate = client_certificate
        private_parameters = _QuerySessionPrivateParameters(**kwargs)
        self.__server_versions = private_parameters.server_versions
        plugins = get_active_plugins().values()
        for plugin in plugins:
            plugin.init_session(self)

    @property
    def cubes(self) -> QueryCubes:
        """Cubes of the session."""
        if self.__cubes is None:
            self.__cubes = create_query_cubes_from_discovery(
                self._discovery,
                execute_gaq=self._execute_gaq if self._gaq_supported else None,
                query_mdx=self.query_mdx,
            )

        return self.__cubes

    @property
    def name(self) -> str:
        """Name of the session."""
        return self._name

    @property
    def url(self) -> str:
        """URL of the session."""
        return self._url

    @property
    def _location(self) -> Mapping[str, Any]:
        return {"url": self.url}

    @property
    def _local_url(self) -> str:
        return self.url

    @property
    def _raw_query_mode_supported(self) -> bool:
        return any(
            version["id"] == "6"
            for version in self._server_versions["apis"]["pivot"]["versions"]
        )

    @property
    def _gaq_supported(self) -> bool:
        return "atoti" in self._server_versions["apis"]

    def _execute_gaq(
        self,
        *,
        cube_name: str,
        measures: Iterable[BaseMeasure],
        levels: Iterable[BaseLevel],
        condition: Optional[BaseCondition] = None,
        include_totals: bool,
        scenario: str,
        timeout: int,
    ) -> pd.DataFrame:
        if include_totals:
            raise ValueError("Totals cannot be included with this query mode.")

        url = self._get_endpoint_url(namespace="atoti", route="arrow/query")
        data = {
            "cubeName": cube_name,
            "branch": scenario,
            "measures": [m.name for m in measures],
            "levelCoordinates": [level._java_description for level in levels],
            **(
                {"equalConditions": {}, "isinConditions": {}}
                if condition is None
                else _serialize_condition(condition)
            ),
            "timeout": timeout,
        }
        return execute_arrow_query(url, data=data, headers=self._auth(url) or {})

    def _generate_auth_headers(self) -> Mapping[str, str]:
        return self._auth(self.url) or {}

    def _execute_json_request(self, url: str, *, body: Optional[Any] = None) -> Any:
        headers = {"Content-Type": "application/json"}
        headers.update(self._auth(url) or {})
        data = json.dumps(body).encode("utf8") if body else None
        # The user can send any URL, wrapping it in a request object makes it a bit safer
        request = Request(url, data=data, headers=headers)
        try:
            with urlopen(request, context=self._ssl_context) as response:  # nosec
                return json.load(response)
        except HTTPError as error:
            error_json = error.read()
            error_data = json.loads(error_json)
            raise RuntimeError("Request failed", error_data) from error

    @property
    def _server_versions(self) -> ServerVersions:
        if self.__server_versions is None:
            url = urljoin(f"{self.url}/", "versions/rest")
            self.__server_versions = cast(
                ServerVersions,
                self._execute_json_request(url),
            )

        return self.__server_versions

    @property
    def _discovery(self) -> Discovery:
        if self.__discovery is None:
            url = self._get_endpoint_url(namespace="pivot", route="cube/discovery")
            response = self._execute_json_request(url)
            self.__discovery = cast(Discovery, response["data"])

        return self.__discovery

    def _query_mdx_to_cellset(self, mdx: str, *, context: Context) -> Cellset:
        url = self._get_endpoint_url(namespace="pivot", route="cube/query/mdx")
        body: Mapping[str, Union[str, Context]] = {"context": context, "mdx": mdx}
        response = self._execute_json_request(url, body=body)
        return cast(Cellset, response["data"])

    @property
    def _ssl_context(self) -> Optional[SSLContext]:
        if self._client_certificate is None:
            return None

        if self.__ssl_context is None:
            self.__ssl_context = _create_ssl_context(self._client_certificate)

        return self.__ssl_context

    def query_mdx(
        self,
        mdx: str,
        *,
        keep_totals: bool = False,
        timeout: int = 30,
        mode: Literal["pretty", "raw"] = "pretty",
        **kwargs: Any,
    ) -> pd.DataFrame:
        private_parameters = _QueryMdxPrivateParameters(**kwargs)
        context = {**private_parameters.context, "queriesTimeLimit": timeout}

        if mode == "raw":
            if not self._raw_query_mode_supported:
                raise ValueError(
                    "`raw` mode not supported by this ActivePivot version."
                )

            url = self._get_endpoint_url(
                namespace="pivot", route="cube/dataexport/download"
            )
            return execute_arrow_query(
                url,
                data={
                    "jsonMdxQuery": {"mdx": mdx, "context": context},
                    "outputConfiguration": {"format": "arrow"},
                },
                headers=self._auth(url) or {},
            )

        cellset = self._query_mdx_to_cellset(mdx, context=context)
        query_result = cellset_to_query_result(
            cellset,
            context=context,
            discovery=self._discovery,
            get_level_java_types=private_parameters.get_level_java_types,
            keep_totals=keep_totals,
        )
        # Let local sessions pass their reference to have the correct name and widget creation code.
        session = private_parameters.session or self
        query_result._atoti_widget_conversion_details = WidgetConversionDetails(
            mdx=mdx,
            session_id=session._id,
            widget_creation_code=session._get_widget_creation_code(),
        )
        return query_result
