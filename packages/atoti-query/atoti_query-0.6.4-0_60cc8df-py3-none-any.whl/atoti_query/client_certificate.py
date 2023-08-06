from dataclasses import dataclass
from typing import Optional

from atoti_core import PathLike, keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class ClientCertificate:
    """A client certificate to open a :class:`~atoti_query.query_session.QuerySession` against a session configured with :class:`~atoti.config.client_certificate.ClientCertificateConfig`.

    Example:

        .. doctest:: client_certificate
            :hide:

            >>> CERTIFICATES_DIRECTORY = (
            ...     _PYTHON_PACKAGES_PATH
            ...     / "atoti-plus"
            ...     / "tests_atoti_plus"
            ...     / "resources"
            ...     / "config"
            ...     / "certificates"
            ... )
            >>> session = tt.create_session(
            ...     config={
            ...         "client_certificate": {
            ...             "trust_store": CERTIFICATES_DIRECTORY / "truststore.jks",
            ...             "trust_store_password": "changeit",
            ...         },
            ...         "https": {
            ...             "certificate": CERTIFICATES_DIRECTORY / "localhost.p12",
            ...             "password": "changeit",
            ...         },
            ...     }
            ... )
            >>> session.security.individual_roles["atoti"] = ["ROLE_USER"]

        .. doctest:: client_certificate

            >>> client_certificate = tt.ClientCertificate(
            ...     certificate=CERTIFICATES_DIRECTORY / "client.pem",
            ...     certificate_authority=CERTIFICATES_DIRECTORY / "root-CA.crt",
            ...     keyfile=CERTIFICATES_DIRECTORY / "client.key",
            ... )
            >>> query_session = tt.QuerySession(
            ...     f"https://localhost:{session.port}",
            ...     client_certificate=client_certificate,
            ... )
    """

    certificate: PathLike
    """Path to the ``.pem`` file containing the client certificate."""

    certificate_authority: Optional[PathLike] = None
    """Path to the custom certificate authority to use to verify the HTTPS connection."""

    keyfile: Optional[PathLike] = None
    """Path to the certificate ``.key`` file."""

    password: Optional[str] = None
    """The certificate password."""
