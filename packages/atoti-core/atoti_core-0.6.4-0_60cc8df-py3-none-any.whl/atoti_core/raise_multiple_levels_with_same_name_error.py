from typing import Any, Iterable, NoReturn

from .base_hierarchy import BaseHierarchy


def raise_multiple_levels_with_same_name_error(
    level_name: str, *, hierarchies: Iterable[BaseHierarchy[Any]]
) -> NoReturn:
    raise KeyError(
        f"""Multiple levels are named {level_name}. Specify the hierarchy (and the dimension if necessary): {", ".join([
            f'cube.levels["{hierarchy.dimension}", "{hierarchy.name}", "{level_name}"]'
            for hierarchy in hierarchies
        ])}"""
    )
