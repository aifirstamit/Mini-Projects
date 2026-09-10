import logging
from pathlib import Path


LOG_FILE = Path(__file__).resolve().parent.parent / "organizer.log"


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_success(message):
    """Log a successful operation."""
    logging.info(f"SUCCESS: {message}")


def log_failure(message):
    """Log a failed operation."""
    logging.error(f"FAILED: {message}")