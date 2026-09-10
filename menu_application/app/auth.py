from .exceptions import LoginError
from .logger import (
    log_debug,
    log_info,
    log_warning,
    log_error,
)


USERNAME = "admin"
PASSWORD = "python123"


def login():
    """Authenticate the user."""

    log_debug("Login operation started.")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username:
        log_warning("Username was empty.")
        raise LoginError("Username cannot be empty.")

    if not password:
        log_warning("Password was empty.")
        raise LoginError("Password cannot be empty.")

    if username == USERNAME and password == PASSWORD:

        log_info("User logged in successfully.")
        return True

    log_error(
        f"Login failed for username: {username}"
    )

    raise LoginError("Invalid username or password.")


def logout():
    """Log the user out."""

    log_info("User logged out.")
    print("Logged out successfully.")