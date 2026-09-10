## Temperature and unit conversion functions.


def validate_number(value):
    """Check whether the value is a number."""

    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("Value must be a number.")


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""

    validate_number(celsius)

    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""

    validate_number(fahrenheit)

    return (fahrenheit - 32) * 5 / 9


def kilometers_to_miles(kilometers):
    """Convert kilometers to miles."""

    validate_number(kilometers)

    if kilometers < 0:
        raise ValueError("Distance cannot be negative.")

    return kilometers * 0.621371


def miles_to_kilometers(miles):
    """Convert miles to kilometers."""

    validate_number(miles)

    if miles < 0:
        raise ValueError("Distance cannot be negative.")

    return miles * 1.60934