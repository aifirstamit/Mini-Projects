from pathlib import Path

from .logger import (
    log_debug,
    log_info,
    log_warning,
    log_error,
)


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def read_file():
    """Read content from a file."""

    log_debug("Read file operation started.")

    filename = input("Enter file name: ").strip()

    file_path = DATA_DIR / filename

    try:
        if not file_path.exists():
            log_error(
                f"File could not be opened: {filename}"
            )
            print("ERROR: File does not exist.")
            return

        content = file_path.read_text(
            encoding="utf-8"
        )

        if not content.strip():
            log_warning(
                f"File was empty: {filename}"
            )
            print("WARNING: File is empty.")
            return

        print("\nFile Content:")
        print(content)

        log_info(
            f"File read successfully: {filename}"
        )

    except PermissionError as error:
        log_error(
            f"Permission denied: {error}"
        )
        print("ERROR: Permission denied.")

    except OSError as error:
        log_error(
            f"File could not be opened: {error}"
        )
        print("ERROR: File could not be opened.")


def write_file():
    """Write content to a file."""

    log_debug("Write file operation started.")

    filename = input("Enter file name: ").strip()

    content = input("Enter content: ")

    if not filename:
        log_warning(
            "Write operation received empty filename."
        )
        print("WARNING: File name cannot be empty.")
        return

    try:
        # Create the data folder if it does not exist
        DATA_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = DATA_DIR / filename

        file_path.write_text(
            content,
            encoding="utf-8"
        )

        log_info(
            f"File written successfully: {filename}"
        )

        print("File written successfully.")

    except PermissionError as error:
        log_error(
            f"Permission denied while writing file: {error}"
        )
        print("ERROR: Permission denied.")

    except OSError as error:
        log_error(
            f"File could not be written: {error}"
        )
        print("ERROR: File could not be written.")