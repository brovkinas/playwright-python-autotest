import re
from pathlib import Path


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


def get_pw_artifacts_dir(request) -> Path | None:
    """
    converts nodeid format to dir-name-pw-uses-to-save-artifacts
    """
    config = request.config
    output_dir = Path(config.option.output)
    nodeid = request.node.nodeid
    nodeid_dir = Path(re.sub(r"[^a-zA-Z0-9]+", "-", nodeid).strip("-"))
    artifacts_dir = output_dir / nodeid_dir

    if not artifacts_dir.exists():
        return None

    return artifacts_dir
