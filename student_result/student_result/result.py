def calculate_total(marks):
    """Calculate total marks."""

    return sum(marks.values())


def calculate_percentage(total, subject_count):
    """Calculate percentage."""

    if subject_count == 0:
        raise ZeroDivisionError(
            "Cannot calculate percentage without subjects."
        )

    return total / (subject_count * 100) * 100


def calculate_grade(percentage):
    """Calculate grade from percentage."""

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


def calculate_status(percentage):
    """Calculate pass or fail status."""

    if percentage >= 40:
        return "PASS"

    return "FAIL"


def calculate_result(marks):
    """Calculate complete student result."""

    total = calculate_total(marks)

    percentage = calculate_percentage(
        total,
        len(marks)
    )

    grade = calculate_grade(percentage)

    status = calculate_status(percentage)

    return {
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status,
    }