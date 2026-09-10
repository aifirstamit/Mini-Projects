from .exceptions import InvalidMarksError, MissingStudentInfoError


SUBJECTS = [
    "Python",
    "Maths",
    "Science",
    "English",
    "Computer",
]


def get_student_name():
    """Read and validate student name."""

    name = input("Enter student name: ").strip()

    if not name:
        raise MissingStudentInfoError(
            "Student name cannot be empty."
        )

    return name


def get_marks(subject):
    """Read and validate marks for one subject."""

    marks_input = input(
        f"Enter marks for {subject}: "
    ).strip()

    if not marks_input:
        raise ValueError(
            f"Marks for {subject} cannot be empty."
        )

    try:
        marks = float(marks_input)

    except ValueError:
        raise ValueError(
            f"Marks for {subject} must be numeric."
        )

    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            f"Marks for {subject} must be between 0 and 100."
        )

    return marks


def get_student_details():
    """Read complete student information."""

    name = get_student_name()

    marks = {}

    for subject in SUBJECTS:
        marks[subject] = get_marks(subject)

    return {
        "name": name,
        "marks": marks,
    }