import logging
import os
from datetime import datetime

LOG_DIR = "logs"


def setup_logger():
    # Create log dir if not exists
    os.makedirs(LOG_DIR, exist_ok=True)

    # Autotests logger
    logger = logging.getLogger("autotests")

    if logger.handlers:
        return logger

    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File handler
    log_file_name = os.path.join(
        LOG_DIR, f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )
    file_handler = logging.FileHandler(log_file_name, encoding="utf-8", mode="a")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("=== AUTOTESTS LOGGER READY ===")

    return logger
