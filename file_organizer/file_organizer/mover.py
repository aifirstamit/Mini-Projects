import shutil
from pathlib import Path

from .logger import log_success, log_failure


def move_file(file_path, destination_folder):
    """Move a file to the destination folder."""

    source = Path(file_path)
    destination = Path(destination_folder)

    try:
        if not source.exists():
            raise FileNotFoundError(
                f"Source file does not exist: {source}"
            )

        if not source.is_file():
            raise ValueError(
                f"Source path is not a file: {source}"
            )

        if not destination.exists():
            raise FileNotFoundError(
                f"Destination folder does not exist: {destination}"
            )

        if not destination.is_dir():
            raise NotADirectoryError(
                f"Destination is not a folder: {destination}"
            )

        target = destination / source.name

        # Handle duplicate filenames
        if target.exists():
            target = get_unique_filename(target)

        shutil.move(str(source), str(target))

        log_success(
            f"Moved '{source.name}' to '{target}'"
        )

        return target

    except PermissionError as error:
        log_failure(
            f"Permission denied while moving '{source}': {error}"
        )
        raise

    except (FileNotFoundError, ValueError, NotADirectoryError) as error:
        log_failure(str(error))
        raise

    except OSError as error:
        log_failure(
            f"OS error while moving '{source}': {error}"
        )
        raise


def get_unique_filename(file_path):
    """Generate a unique filename if a duplicate exists."""

    path = Path(file_path)

    counter = 1

    while True:
        new_name = (
            f"{path.stem}_{counter}{path.suffix}"
        )

        new_path = path.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1