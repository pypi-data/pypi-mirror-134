import sys
from typing import cast

from .get_top_level_package_name import get_top_level_package_name

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version


def get_package_version(module_name: str) -> str:
    """Return the version of the package where *module_name* is the ``__name__`` of one of its modules."""
    package_name = get_top_level_package_name(module_name)
    return cast(
        str,
        version(package_name),  # type: ignore[no-untyped-call]
    )
