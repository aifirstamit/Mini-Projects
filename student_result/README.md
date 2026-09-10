# 🎓 Student Result Processing System

A Python-based **Student Result Processing System** that reads student details and marks for five subjects, validates the input, calculates results, handles errors using exceptions, and records errors and successful operations using logging.

The project is designed using **Python packages and modules** to demonstrate clean code organization and separation of responsibilities.

---

## 📌 Project Overview

The program accepts:

* Student name
* Marks for 5 subjects

It then calculates:

* Total marks
* Percentage
* Grade
* Pass/Fail status

The program also handles invalid inputs such as:

* Missing student information
* Non-numeric marks
* Marks below `0`
* Marks above `100`
* Calculation errors
* Other unexpected errors

If an error occurs for one student, the program **logs the error and continues processing the remaining students**.

---

## 🎯 Learning Objectives

This project demonstrates the following Python concepts:

* Functions
* Modules
* Packages
* Importing modules
* Dictionaries
* Lists
* Loops
* User input
* Input validation
* Exception handling
* Custom exceptions
* Logging
* Separation of responsibilities
* Error recovery and continuation

---

## 📁 Project Structure

```text
student_result/
│
├── student_result/
│   ├── __init__.py
│   ├── student.py
│   ├── result.py
│   ├── exceptions.py
│   └── logger.py
│
├── main.py
├── README.md
└── student_result.log
```

---

## 🧩 Module Responsibilities

### `student.py`

Responsible for:

* Reading student information
* Reading marks for five subjects
* Validating student name
* Validating marks
* Detecting non-numeric input
* Detecting marks outside the `0–100` range

---

### `result.py`

Responsible for:

* Calculating total marks
* Calculating percentage
* Calculating grade
* Calculating pass/fail status

---

### `exceptions.py`

Contains custom exceptions used by the application.

Example:

```python
class InvalidMarksError(Exception):
    """Raised when marks are outside the valid range."""

    pass
```

Another custom exception is used for missing student information:

```python
class MissingStudentInfoError(Exception):
    """Raised when required student information is missing."""

    pass
```

---

### `logger.py`

Responsible for configuring logging and recording:

* Successful student processing
* Invalid input
* Validation errors
* Calculation errors
* Unexpected errors

Logs are stored in:

```text
student_result.log
```

---

### `main.py`

Acts as the main application controller.

It:

1. Asks for the number of students.
2. Processes students one by one.
3. Calls the required modules.
4. Calculates the result.
5. Displays the result.
6. Handles exceptions.
7. Logs errors.
8. Continues processing the next student.

---

# 📚 Subjects

The program processes five subjects:

```text
Python
Maths
Science
English
Computer
```

Each subject accepts marks between:

```text
0 - 100
```

---

# 📊 Grade System

The following grading system is used:

| Percentage | Grade |
| ---------: | :---- |
|     90–100 | A+    |
|      80–89 | A     |
|      70–79 | B     |
|      60–69 | C     |
|      50–59 | D     |
|   Below 50 | F     |

---

# ✅ Pass/Fail Criteria

A student is considered **PASS** when the percentage is:

```text
40% or above
```

Otherwise:

```text
FAIL
```

---

# 🧮 Result Calculation

For example:

```text
Python     = 80
Maths      = 70
Science    = 90
English    = 85
Computer   = 75
```

### Total

```text
80 + 70 + 90 + 85 + 75 = 400
```

### Maximum Marks

```text
5 × 100 = 500
```

### Percentage

```text
400 / 500 × 100 = 80%
```

### Final Result

```text
Total      : 400
Percentage : 80%
Grade      : A
Status     : PASS
```

---

# ⚠️ Error Handling

The application handles several types of errors.

## 1. Missing Student Name

If the user does not enter a name:

```text
ERROR: Student name cannot be empty.
```

---

## 2. Non-Numeric Marks

If the user enters:

```text
abc
```

instead of a number:

```text
INPUT ERROR: Marks for Python must be numeric.
```

---

## 3. Marks Below 0

Example:

```text
-10
```

Result:

```text
ERROR: Marks for Python must be between 0 and 100.
```

---

## 4. Marks Above 100

Example:

```text
150
```

Result:

```text
ERROR: Marks for Maths must be between 0 and 100.
```

---

## 5. Calculation Error

The program also handles calculation-related errors such as:

```python
ZeroDivisionError
```

This prevents the program from crashing unexpectedly.

---

# 🔄 Continue Processing After Errors

One of the most important requirements of this project is that an error for one student should **not stop the complete program**.

For example:

```text
Student 1
    ↓
Valid
    ↓
Result calculated


Student 2
    ↓
Invalid marks
    ↓
Error logged
    ↓
Continue


Student 3
    ↓
Valid
    ↓
Result calculated
```

This is achieved by processing each student separately:

```python
for student_number in range(1, student_count + 1):
    process_student(student_number)
```

Each student has its own exception handling.

---

# 📝 Logging

Every important operation is recorded in:

```text
student_result.log
```

Example:

```text
2026-09-10 23:10:20 - INFO - SUCCESS: Processed student: Amit
2026-09-10 23:10:35 - ERROR - ERROR: Marks for Maths must be between 0 and 100.
2026-09-10 23:11:02 - INFO - SUCCESS: Processed student: Rahul
```

Logging makes it possible to track what happened during program execution.

---

# 🚀 How to Run

## Step 1: Open the Project

Open the project folder in VS Code.

```powershell
cd "$HOME\Desktop\student_result"
```

---

## Step 2: Run the Program

```powershell
python main.py
```

---

## Step 3: Enter Number of Students

Example:

```text
Enter number of students: 2
```

---

## Step 4: Enter Student Details

Example:

```text
--- Student 1 ---
Enter student name: Amit
Enter marks for Python: 85
Enter marks for Maths: 90
Enter marks for Science: 80
Enter marks for English: 75
Enter marks for Computer: 95
```

---

# 💻 Sample Output

```text
==================================================
       STUDENT RESULT PROCESSOR
==================================================

--- Student 1 ---
Enter student name: Amit
Enter marks for Python: 85
Enter marks for Maths: 90
Enter marks for Science: 80
Enter marks for English: 75
Enter marks for Computer: 95

==================================================
             STUDENT RESULT
==================================================
Name       : Amit
Total      : 425.00
Percentage : 85.00%
Grade      : A
Status     : PASS
==================================================

All students have been processed.
```

---

# 🧪 Example Error Test

Input:

```text
Enter marks for Python: abc
```

Output:

```text
INPUT ERROR: Marks for Python must be numeric.
```

The program then continues with the next student.

---

# 🏗️ Program Flow

```text
Start
  │
  ▼
Enter number of students
  │
  ▼
Process Student
  │
  ▼
Read Student Name
  │
  ▼
Read 5 Subject Marks
  │
  ▼
Validate Input
  │
  ├── Invalid ──► Raise Exception
  │                    │
  │                    ▼
  │                Log Error
  │                    │
  │                    ▼
  │              Continue Next Student
  │
  ▼
Calculate Total
  │
  ▼
Calculate Percentage
  │
  ▼
Calculate Grade
  │
  ▼
Calculate Pass/Fail
  │
  ▼
Display Result
  │
  ▼
Log Success
  │
  ▼
Next Student
  │
  ▼
End
```

---

# 🔑 Key Concepts

## 1. Custom Exceptions

```python
class InvalidMarksError(Exception):
    pass
```

Used to represent application-specific validation errors.

---

## 2. Exception Handling

```python
try:
    student = get_student_details()
    result = calculate_result(student["marks"])

except InvalidMarksError as error:
    log_error(str(error))
    print(f"ERROR: {error}")
```

---

## 3. Logging

```python
log_success("Processed student successfully")
```

and:

```python
log_error("Invalid marks entered")
```

---

## 4. Modules

The project separates functionality into different Python files:

```text
student.py
result.py
exceptions.py
logger.py
```

This makes the application easier to understand and maintain.

---

## 5. Package

The `student_result` folder contains:

```text
__init__.py
student.py
result.py
exceptions.py
logger.py
```

Because it contains `__init__.py`, it can be used as a Python package.

---

# 🧠 Separation of Responsibilities

Each module has a specific job:

```text
student.py
    ↓
Input + Validation

result.py
    ↓
Calculations

exceptions.py
    ↓
Custom Errors

logger.py
    ↓
Logging

main.py
    ↓
Application Control
```

This approach avoids putting the entire program into one large Python file.

---

# 🛠️ Technologies Used

* Python 3
* Python Standard Library
* `pathlib`
* `logging`
* Exception Handling
* Custom Exceptions
* Modules
* Packages

No external Python packages are required.

---

# 🚀 Future Improvements

Possible future enhancements:

* Store student results in CSV
* Export results to Excel
* Add student roll numbers
* Add individual subject grades
* Generate report cards
* Add a graphical user interface
* Store results in a database
* Add unit tests
* Add command-line arguments
* Create a web-based student result system

---

# 📌 What This Project Demonstrates

This project demonstrates how Python can be used to build a small but structured application using:

```text
Packages
   +
Modules
   +
Functions
   +
Input Validation
   +
Custom Exceptions
   +
Exception Handling
   +
Logging
   +
Loops
```

The main goal is not only to calculate student marks, but to learn how to build a **reliable, modular Python application that can handle errors without stopping the entire program**.

---

## 👨‍💻 Author

**AI First**

> Learn AI. Build AI. Shape the Future.

---

## 📄 License

This project is created for **learning and educational purposes**.
