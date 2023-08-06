from base64 import b64encode
from dataclasses import dataclass
from typing import cast

from atoti_core import keyword_only_dataclass

from .auth import Auth, HttpHeaders
from .token_authentication import TokenAuthentication


@keyword_only_dataclass
@dataclass(frozen=True, eq=False)
class BasicAuthentication(Auth):
    username: str
    password: str

    def __call__(self, url: str) -> HttpHeaders:
        return self._token_authentication(url)

    @property
    def _token_authentication(self) -> TokenAuthentication:
        property_name = "_token_authentication"

        if property_name not in self.__dict__:
            plain_credentials = f"{self.username}:{self.password}"
            token = str(b64encode(plain_credentials.encode("ascii")), "utf8")
            self.__dict__[property_name] = TokenAuthentication(  # nosec
                token=token, token_type="Basic"
            )

        return cast(TokenAuthentication, self.__dict__[property_name])
