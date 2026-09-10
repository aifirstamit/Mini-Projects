from .logger import (
    log_debug,
    log_info,
    log_error,
)


def calculate():
    """Perform a calculation."""

    log_debug("Calculation operation started.")

    try:
        first_number = float(
            input("Enter first number: ")
        )

        second_number = float(
            input("Enter second number: ")
        )

        operator = input(
            "Enter operator (+, -, *, /): "
        ).strip()

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            result = first_number / second_number

        else:
            log_error(
                f"Unsupported operator: {operator}"
            )

            print("Invalid operator.")
            return

        print(f"Result: {result}")

        log_info("Calculation completed.")

    except ValueError as error:

        log_error(
            f"Invalid numeric input: {error}"
        )

        print(
            "ERROR: Please enter valid numbers."
        )

    except ZeroDivisionError as error:

        log_error(
            f"Division by zero: {error}"
        )

        print(
            "ERROR: Cannot divide by zero."
        )