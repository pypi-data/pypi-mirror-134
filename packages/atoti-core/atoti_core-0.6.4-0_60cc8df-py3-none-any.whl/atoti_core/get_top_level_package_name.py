def get_top_level_package_name(module_name: str) -> str:
    """Return the name of the package (without dots) where *module_name* is the ``__name__`` of one of its modules."""
    return module_name.split(".", maxsplit=1)[0]
