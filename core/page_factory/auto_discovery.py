import importlib
import pkgutil
import logging
import pages

logger = logging.getLogger("autotests")

_DISCOVERED = False


def auto_discover_pages() -> None:

    global _DISCOVERED
    if _DISCOVERED:
        return
    _DISCOVERED = True

    for module_info in pkgutil.walk_packages(
        pages.__path__,
        pages.__name__ + ".",
    ):
        module_name = module_info.name

        # if ".page_factory." in module_name or not module_name.endswith("_page"):
        if not module_name.split(".")[-1].endswith("_page"):
            continue

        try:
            logger.debug(f"Auto-discovering page module: {module_name}")
            importlib.import_module(module_name)

        except Exception:
            logger.exception(f"Failed to import {module_name}")
            raise
