from student_result import (
    get_student_details,
    calculate_result,
    InvalidMarksError,
    MissingStudentInfoError,
    log_success,
    log_error,
)


def display_result(student, result):
    """Display the student's result."""

    print("\n" + "=" * 50)
    print("             STUDENT RESULT")
    print("=" * 50)

    print(f"Name       : {student['name']}")
    print(f"Total      : {result['total']:.2f}")
    print(f"Percentage : {result['percentage']:.2f}%")
    print(f"Grade      : {result['grade']}")
    print(f"Status     : {result['status']}")

    print("=" * 50)


def process_student(student_number):
    """Read and process one student."""

    print(f"\n--- Student {student_number} ---")

    try:
        student = get_student_details()

        result = calculate_result(
            student["marks"]
        )

        display_result(
            student,
            result
        )

        log_success(
            f"Processed student: {student['name']}"
        )

    except InvalidMarksError as error:
        log_error(str(error))
        print(f"ERROR: {error}")

    except MissingStudentInfoError as error:
        log_error(str(error))
        print(f"ERROR: {error}")

    except ValueError as error:
        log_error(str(error))
        print(f"INPUT ERROR: {error}")

    except ZeroDivisionError as error:
        log_error(str(error))
        print(f"CALCULATION ERROR: {error}")

    except OSError as error:
        log_error(str(error))
        print(f"SYSTEM ERROR: {error}")

    except Exception as error:
        log_error(
            f"Unexpected error: {error}"
        )
        print(
            f"UNEXPECTED ERROR: {error}"
        )


def main():
    print("=" * 50)
    print("       STUDENT RESULT PROCESSOR")
    print("=" * 50)

    try:
        student_count = int(
            input("Enter number of students: ")
        )

        if student_count <= 0:
            print("Number of students must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    for student_number in range(1, student_count + 1):

        process_student(student_number)

    print("\nAll students have been processed.")


if __name__ == "__main__":
    main()