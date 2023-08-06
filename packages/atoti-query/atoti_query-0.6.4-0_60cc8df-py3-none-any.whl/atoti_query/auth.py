from typing import Mapping, Optional

from typing_extensions import Protocol

HttpHeaders = Optional[Mapping[str, str]]


class Auth(Protocol):
    """Called with the URL of the request and returning the HTTP headers necessary to authenticate it.

    There are some built-in implementations:

    * :class:`~atoti_query.basic_authentication.BasicAuthentication`
    * :class:`~atoti_query.token_authentication.TokenAuthentication`
    """

    def __call__(self, url: str) -> HttpHeaders:
        ...
