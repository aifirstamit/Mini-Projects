class ApplicationError(Exception):
    """Base exception for application-specific errors."""

    pass


class LoginError(ApplicationError):
    """Raised when login fails."""

    pass