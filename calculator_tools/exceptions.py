## Custom exception for invalid calculator operations.


class InvalidOperationError(Exception):
    """Raised when an unsupported operation is requested."""

    pass