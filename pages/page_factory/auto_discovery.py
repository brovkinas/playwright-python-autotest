import importlib
import pkgutil
import logging

import pages

logger = logging.getLogger("autotests")


def discover_pages() -> None:
    """
    Automatically imports all page modules
    """

    for module_info in pkgutil.walk_packages(
        pages.__path__,
        pages.__name__ + ".",
    ):
        module_name = module_info.name

        if ".page_factory." in module_name:
            continue

        logger.debug(f"Auto-discovering page module: {module_name}")
        importlib.import_module(module_name)
