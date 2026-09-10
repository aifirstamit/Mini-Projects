## Question: Build your own calculator_tools Python package.
## Import the package and demonstrate all functionality.


from calculator_tools import add
from calculator_tools import subtract
from calculator_tools import multiply
from calculator_tools import divide
from calculator_tools import calculate_percentage
from calculator_tools import calculate_average
from calculator_tools import celsius_to_fahrenheit
from calculator_tools import fahrenheit_to_celsius
from calculator_tools import kilometers_to_miles
from calculator_tools import miles_to_kilometers
from calculator_tools import calculate_operation
from calculator_tools import InvalidOperationError


def main():
    """Demonstrate all calculator_tools package functionality."""

    print("===== Arithmetic Operations =====")

    print("Addition:", add(10, 20))
    print("Subtraction:", subtract(20, 10))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(20, 5))

    print()
    print("===== Percentage =====")

    print("20% of 500:", calculate_percentage(500, 20))

    print()
    print("===== Average =====")

    numbers = [10, 20, 30, 40, 50]

    print("Numbers:", numbers)
    print("Average:", calculate_average(numbers))

    print()
    print("===== Temperature Conversion =====")

    print(
        "25 Celsius to Fahrenheit:",
        celsius_to_fahrenheit(25)
    )

    print(
        "77 Fahrenheit to Celsius:",
        fahrenheit_to_celsius(77)
    )

    print()
    print("===== Unit Conversion =====")

    print(
        "10 Kilometers to Miles:",
        kilometers_to_miles(10)
    )

    print(
        "10 Miles to Kilometers:",
        miles_to_kilometers(10)
    )

    print()
    print("===== Operation Selection =====")

    print(
        "Add:",
        calculate_operation("add", 100, 50)
    )

    print(
        "Multiply:",
        calculate_operation("multiply", 10, 5)
    )

    print()
    print("===== Error Handling =====")

    try:
        divide(10, 0)

    except ZeroDivisionError as error:
        print("Error:", error)

    try:
        add(10, "20")

    except TypeError as error:
        print("Error:", error)

    try:
        calculate_average([])

    except ValueError as error:
        print("Error:", error)

    try:
        calculate_operation("power", 10, 2)

    except InvalidOperationError as error:
        print("Error:", error)


main()


# Sample Output:
#
# ===== Arithmetic Operations =====
# Addition: 30
# Subtraction: 10
# Multiplication: 50
# Division: 4.0
#
# ===== Percentage =====
# 20% of 500: 100.0
#
# ===== Average =====
# Numbers: [10, 20, 30, 40, 50]
# Average: 30.0
#
# ===== Temperature Conversion =====
# 25 Celsius to Fahrenheit: 77.0
# 77 Fahrenheit to Celsius: 25.0
#
# ===== Unit Conversion =====
# 10 Kilometers to Miles: 6.21371
# 10 Miles to Kilometers: 16.0934
#
# ===== Operation Selection =====
# Add: 150
# Multiply: 50
#
# ===== Error Handling =====
# Error: Cannot divide by zero.
# Error: Second value must be a number.
# Error: Cannot calculate average of an empty list.
# Error: Unsupported operation: power