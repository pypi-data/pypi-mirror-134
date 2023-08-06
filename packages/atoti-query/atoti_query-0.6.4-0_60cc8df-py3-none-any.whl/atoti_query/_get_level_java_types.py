from typing import Iterable, Mapping

from atoti_core import CubeName, JavaType, LevelCoordinates
from typing_extensions import Protocol


class GetLevelJavaTypes(Protocol):
    def __call__(
        self, levels_coordinates: Iterable[LevelCoordinates], *, cube_name: CubeName
    ) -> Mapping[LevelCoordinates, JavaType]:
        ...
