from pathlib import Path
from _pytest.nodes import Item
from core.stash_keys import PW_OUTPUT_DIR


def project_root(
    start: Path = None, markers=("pyproject.toml", "requirements.txt", ".gitignore")
):
    if start is None:
        start = Path(__file__).resolve()

    current = start

    while current != current.parent:
        for marker in markers:
            if (current / marker).exists():
                return current

        current = current.parent

    raise RuntimeError("Project root not found")


def nodeid_to_dir_path(item: Item) -> Path:

    output_dir = item.config.stash[PW_OUTPUT_DIR]

    name = item.nodeid
    name = (
        name.replace("::", "-")
        .replace("/", "-")
        .replace(".", "-")
        .replace("[", "-")
        .replace("]", "")
    )

    return Path(output_dir) / name
