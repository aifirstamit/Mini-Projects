from pathlib import Path
from .exceptions import UnsupportedFileError


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx"],
    "Text": [".txt", ".md"],
    "Data": [".csv", ".xlsx", ".json"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"],
}


def detect_category(file_path):
    """Return the category folder for a file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File does not exist: {file_path}"
        )

    if not path.is_file():
        raise ValueError(
            f"Path is not a file: {file_path}"
        )

    extension = path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    raise UnsupportedFileError(
        f"Unsupported file type: {extension or 'No extension'}"
    )