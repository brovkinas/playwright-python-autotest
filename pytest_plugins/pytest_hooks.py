import os
import time

import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    timestamp = int(time.time() * 1000)
    output_dir = f"test-results-{timestamp}"

    config.option.output = output_dir
    os.environ["ALLURE_RESULTS_DIR"] = output_dir

    # save in config for hooks access
    config._playwright_output_dir = output_dir

    # GitHub Actions support
    github_env = os.getenv("GITHUB_ENV")
    if github_env:
        with open(github_env, "a", encoding="utf-8") as f:
            f.write(f"ALLURE_RESULTS_DIR={output_dir}\n")
