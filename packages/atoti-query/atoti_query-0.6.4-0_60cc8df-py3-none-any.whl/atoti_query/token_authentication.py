from dataclasses import dataclass
from typing import cast

from atoti_core import keyword_only_dataclass

from .auth import Auth, HttpHeaders


@keyword_only_dataclass
@dataclass(frozen=True, eq=False)
class TokenAuthentication(Auth):
    token: str
    token_type: str = "Bearer"

    def __call__(self, url: str) -> HttpHeaders:
        return self._headers

    @property
    def _headers(self) -> HttpHeaders:
        property_name = "_headers"

        if property_name not in self.__dict__:
            self.__dict__[property_name] = {
                "Authorization": f"{self.token_type} {self.token}"
            }

        return cast(HttpHeaders, self.__dict__[property_name])
