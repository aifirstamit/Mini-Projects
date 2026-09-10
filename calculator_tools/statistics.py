## Statistics functions for the calculator_tools package.


def calculate_average(numbers):
    """Return the average of a list of numbers."""

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list.")

    total = 0

    for number in numbers:

        if not isinstance(number, (int, float)) or isinstance(number, bool):
            raise TypeError("All values must be numbers.")

        total = total + number

    return total / len(numbers)