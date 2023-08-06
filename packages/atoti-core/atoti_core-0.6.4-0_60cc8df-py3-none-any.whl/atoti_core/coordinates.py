from typing import Tuple, Union

CubeName = str

DimensionName = str

HierarchyName = str
HierarchyCoordinates = Tuple[DimensionName, HierarchyName]

HierarchyKey = Union[HierarchyName, HierarchyCoordinates]

LevelName = str
LevelCoordinates = Tuple[DimensionName, HierarchyName, LevelName]

LevelKey = Union[LevelName, Tuple[HierarchyName, LevelName], LevelCoordinates]


def get_java_coordinates(level_coordinates: LevelCoordinates) -> str:
    """Get the corresponding string that can be used to identify the level in Java."""
    return "@".join(reversed(level_coordinates))
