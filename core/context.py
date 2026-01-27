from dataclasses import dataclass
from typing import Optional

from playwright.sync_api import Page


@dataclass
class TestContext:
    nodeid: str
    artifacts_dir: Optional[str] = None
    page: Optional[Page] = None
    log_file: Optional[str] = None
