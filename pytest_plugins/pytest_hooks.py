import os
import pytest

from core.stash_keys import PW_OUTPUT_DIR
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):

    if not hasattr(config, "workerinput"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pw_output_dir = f"test-results-{timestamp}"

        os.environ["PW_OUTPUT_DIR"] = pw_output_dir

        # GitHub Actions
        github_env = os.getenv("GITHUB_ENV")
        if github_env:
            with open(github_env, "a", encoding="utf-8") as f:
                f.write(f"PW_OUTPUT_DIR={pw_output_dir}\n")
    else:
        pw_output_dir = os.environ.get("PW_OUTPUT_DIR")

        if not pw_output_dir:
            raise RuntimeError("PW_OUTPUT_DIR not set")

    config.stash[PW_OUTPUT_DIR] = pw_output_dir
    config.option.output = pw_output_dir
