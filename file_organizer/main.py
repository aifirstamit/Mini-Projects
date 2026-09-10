from pathlib import Path

from file_organizer import (
    detect_category,
    move_file,
    UnsupportedFileError,
)
from file_organizer.logger import log_failure


def organize_folder(source_folder):
    """Organize files in the given folder."""

    source = Path(source_folder)

    if not source.exists():
        raise FileNotFoundError(
            f"Source folder does not exist: {source}"
        )

    if not source.is_dir():
        raise NotADirectoryError(
            f"Source path is not a folder: {source}"
        )

    for file_path in source.iterdir():

        if not file_path.is_file():
            continue

        try:
            category = detect_category(file_path)

            destination = source / category

            # Create destination folder if needed
            destination.mkdir(
                parents=True,
                exist_ok=True
            )

            move_file(
                file_path,
                destination
            )

            print(
                f"SUCCESS: {file_path.name} -> {category}/"
            )

        except UnsupportedFileError as error:
            log_failure(str(error))
            print(
                f"FAILED: {file_path.name} - {error}"
            )

        except PermissionError as error:
            log_failure(str(error))
            print(
                f"PERMISSION ERROR: {file_path.name} - {error}"
            )

        except FileNotFoundError as error:
            log_failure(str(error))
            print(
                f"FILE ERROR: {file_path.name} - {error}"
            )

        except OSError as error:
            log_failure(str(error))
            print(
                f"OS ERROR: {file_path.name} - {error}"
            )


def main():
    print("=" * 50)
    print("          FILE ORGANIZER")
    print("=" * 50)

    # Change this to the folder you want to organize.
    source_folder = Path("test_files")

    try:
        organize_folder(source_folder)

    except FileNotFoundError as error:
        log_failure(str(error))
        print(f"ERROR: {error}")

    except NotADirectoryError as error:
        log_failure(str(error))
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()