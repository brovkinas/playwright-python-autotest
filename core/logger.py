import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def setup_logger():
    # ROOT logger
    root_logger = logging.getLogger()

    # remove handlers pytest
    for h in list(root_logger.handlers):
        root_logger.removeHandler(h)

    root_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    # File
    file_name = f"{LOG_DIR}/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(file_name, encoding="utf-8", mode="a")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console)
    root_logger.addHandler(file_handler)

    root_logger.info("=== ROOT LOGGER READY ===")

    return root_logger
