import logging
from pathlib import Path


LOG_DIR = Path(__file__).resolve().parent.parent / "logs"

APPLICATION_LOG = LOG_DIR / "application.log"
ERROR_LOG = LOG_DIR / "error.log"


LOG_DIR.mkdir(exist_ok=True)


logger = logging.getLogger("menu_application")
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)


application_handler = logging.FileHandler(
    APPLICATION_LOG,
    encoding="utf-8"
)

application_handler.setLevel(logging.DEBUG)
application_handler.setFormatter(formatter)


error_handler = logging.FileHandler(
    ERROR_LOG,
    encoding="utf-8"
)

error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)


logger.addHandler(application_handler)
logger.addHandler(error_handler)


def log_debug(message):
    """Log a DEBUG message."""

    logger.debug(message)


def log_info(message):
    """Log an INFO message."""

    logger.info(message)


def log_warning(message):
    """Log a WARNING message."""

    logger.warning(message)


def log_error(message):
    """Log an ERROR message."""

    logger.error(message)


def log_critical(message):
    """Log a CRITICAL message."""

    logger.critical(message)