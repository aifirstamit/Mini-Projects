## Arithmetic functions for the calculator_tools package.


from .exceptions import InvalidOperationError


def add(a, b):
    """Return the addition of two numbers."""

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("First value must be a number.")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Second value must be a number.")

    return a + b


def subtract(a, b):
    """Return the subtraction of two numbers."""

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("First value must be a number.")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Second value must be a number.")

    return a - b


def multiply(a, b):
    """Return the multiplication of two numbers."""

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("First value must be a number.")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Second value must be a number.")

    return a * b


def divide(a, b):
    """Return the division of two numbers."""

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("First value must be a number.")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Second value must be a number.")

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def calculate_percentage(value, percentage):
    """Return the given percentage of a value."""

    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("Value must be a number.")

    if not isinstance(percentage, (int, float)) or isinstance(percentage, bool):
        raise TypeError("Percentage must be a number.")

    if percentage < 0:
        raise ValueError("Percentage cannot be negative.")

    return value * percentage / 100


def calculate_operation(operation, a, b):
    """Perform an operation based on the operation name."""

    if operation == "add":
        return add(a, b)

    elif operation == "subtract":
        return subtract(a, b)

    elif operation == "multiply":
        return multiply(a, b)

    elif operation == "divide":
        return divide(a, b)

    else:
        raise InvalidOperationError(
            "Unsupported operation: " + str(operation)
        )