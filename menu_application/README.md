# 🧾 Menu-Driven Python Application with Logging

A Python-based **menu-driven application** that allows users to perform different operations such as login, calculation, reading files, writing files, and logout.

The primary focus of this project is **Python logging**. The application demonstrates all five standard logging levels:

* `DEBUG`
* `INFO`
* `WARNING`
* `ERROR`
* `CRITICAL`

The project also demonstrates **exception handling, custom exceptions, modules, packages, file operations, and error recovery**.

---

## 📌 Project Overview

The application provides the following menu:

```text
1. Login
2. Calculate
3. Read a File
4. Write a File
5. Logout
```

The application records important events and errors in separate log files.

```text
logs/
├── application.log
└── error.log
```

A major requirement of this project is that an error in one operation should **not terminate the entire application**.

Instead, the application:

```text
Detect Error
     ↓
Handle Exception
     ↓
Log Error
     ↓
Display Message
     ↓
Continue Application
```

---

## 🎯 Learning Objectives

This project demonstrates:

* Python functions
* Python modules
* Python packages
* Importing modules
* Menu-driven applications
* `while` loops
* Conditional statements
* User input
* Input validation
* Exception handling
* Custom exceptions
* File handling
* Python `logging`
* Logging levels
* Multiple log handlers
* Separate log files
* Error recovery
* Separation of responsibilities

---

## 📁 Project Structure

```text
menu_application/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── calculator.py
│   ├── file_operations.py
│   ├── logger.py
│   └── exceptions.py
│
├── logs/
│   ├── application.log
│   └── error.log
│
├── data/
│   └── sample.txt
│
├── main.py
└── README.md
```

---

## 🧩 Module Responsibilities

### `auth.py`

Responsible for:

* User login
* Username validation
* Password validation
* Logout
* Login-related logging

---

### `calculator.py`

Responsible for:

* Reading numbers
* Reading mathematical operators
* Addition
* Subtraction
* Multiplication
* Division
* Handling invalid numeric input
* Handling division by zero

---

### `file_operations.py`

Responsible for:

* Reading files
* Writing files
* Detecting missing files
* Detecting empty files
* Handling file permission errors
* Logging file operations

---

### `logger.py`

Responsible for:

* Configuring the application logger
* Creating log handlers
* Setting logging levels
* Writing application logs
* Writing error logs

---

### `exceptions.py`

Responsible for defining custom application exceptions.

Example:

```python
class ApplicationError(Exception):
    """Base exception for application-specific errors."""

    pass
```

Login-specific errors are handled using:

```python
class LoginError(ApplicationError):
    """Raised when login fails."""

    pass
```

---

### `main.py`

Acts as the main controller of the application.

It is responsible for:

* Displaying the menu
* Reading the user's choice
* Controlling application flow
* Checking login status
* Calling functions from other modules
* Handling unexpected errors
* Keeping the application running

---

# 📋 Application Menu

The application provides five options:

```text
========================================
       MENU-DRIVEN APPLICATION
========================================
1. Login
2. Calculate
3. Read a File
4. Write a File
5. Logout
========================================
```

---

# 🔐 1. Login

The user can log into the application using predefined credentials.

Example:

```text
Username: admin
Password: python123
```

Successful login generates an `INFO` log:

```text
INFO - User logged in successfully.
```

An unsuccessful login generates an `ERROR` log.

---

# 🧮 2. Calculate

The calculator supports:

```text
+
-
*
/
```

Example:

```text
Enter first number: 10
Enter second number: 20
Enter operator (+, -, *, /): +
```

Output:

```text
Result: 30.0
```

A successful calculation generates:

```text
INFO - Calculation completed.
```

---

## ⚠️ Division by Zero

If the user enters:

```text
Enter first number: 10
Enter second number: 0
Enter operator (+, -, *, /): /
```

The application displays:

```text
ERROR: Cannot divide by zero.
```

The error is logged, but the application continues running.

---

# 📖 3. Read a File

The application can read files stored inside:

```text
data/
```

Example:

```text
Enter file name: sample.txt
```

The application reads and displays the file contents.

A successful operation generates an `INFO` log:

```text
INFO - File read successfully: sample.txt
```

---

## ⚠️ Empty File

If the selected file contains no content:

```text
WARNING: File is empty.
```

The application generates:

```text
WARNING - File was empty: empty.txt
```

The program continues running normally.

---

## ❌ Missing File

If the user enters a file that doesn't exist:

```text
Enter file name: missing.txt
```

The application displays:

```text
ERROR: File does not exist.
```

The error is recorded in the log.

---

# ✍️ 4. Write a File

The application can create or update files inside:

```text
data/
```

Example:

```text
Enter file name: notes.txt
Enter content: Python logging is easy to understand.
```

Output:

```text
File written successfully.
```

The application records:

```text
INFO - File written successfully: notes.txt
```

---

# 🚪 5. Logout

The logout option ends the current session.

Example:

```text
Logged out successfully.
```

The application records:

```text
INFO - User logged out.
```

---

# 📝 Logging

Logging is the main focus of this project.

Python provides five commonly used logging levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

## 🔍 DEBUG

`DEBUG` provides detailed information useful during development and troubleshooting.

Example:

```python
log_debug("Application started.")
```

Log:

```text
DEBUG - Application started.
```

---

## ℹ️ INFO

`INFO` represents normal successful application activity.

Example:

```python
log_info("User logged in successfully.")
```

Log:

```text
INFO - User logged in successfully.
```

---

## ⚠️ WARNING

`WARNING` indicates something unexpected happened, but the application can continue.

Example:

```python
log_warning("File was empty.")
```

Log:

```text
WARNING - File was empty.
```

---

## ❌ ERROR

`ERROR` indicates that an operation failed.

Example:

```python
log_error("File could not be opened.")
```

Log:

```text
ERROR - File could not be opened.
```

---

## 🚨 CRITICAL

`CRITICAL` represents a serious application-level problem.

Example:

```python
log_critical("Unexpected application failure.")
```

Log:

```text
CRITICAL - Unexpected application failure.
```

---

# 📊 Logging Hierarchy

The severity levels can be visualized as:

```text
DEBUG
  ↓
INFO
  ↓
WARNING
  ↓
ERROR
  ↓
CRITICAL
```

As we move downward, the severity increases.

---

# 📂 Log File Configuration

The application stores logs in:

```text
logs/
├── application.log
└── error.log
```

### `application.log`

Stores all logging levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

### `error.log`

Stores only serious errors:

```text
ERROR
CRITICAL
```

This allows normal application activity and serious errors to be reviewed separately.

---

# 🔄 Logging Flow

```text
Application
     │
     ▼
Logger
     │
     ├───────────────┐
     ▼               ▼
application.log   error.log
     │               │
     ▼               ▼
DEBUG              ERROR
INFO               CRITICAL
WARNING
ERROR
CRITICAL
```

---

# 🛡️ Exception Handling

The application uses `try-except` blocks to prevent errors from terminating the entire program.

Example:

```python
try:
    calculate()

except Exception as error:
    log_critical(
        f"Unexpected application failure: {error}"
    )

    print(
        "CRITICAL: Unexpected application failure."
    )
```

The important concept is:

```text
Error occurs
     ↓
Exception caught
     ↓
Error logged
     ↓
Error displayed
     ↓
Menu appears again
```

---

# 🔁 Continue After Errors

The application is designed so that one failed operation does not terminate the entire application.

For example:

```text
Login
  ↓
Success
  ↓
Calculate
  ↓
Division by zero
  ↓
Error logged
  ↓
Return to menu
  ↓
Read File
  ↓
Continue normally
```

This makes the application more reliable.

---

# 🔒 Login Requirement

The calculator and file operations require the user to be logged in.

If the user tries to calculate without logging in:

```text
Please login first.
```

The application records the event and returns to the menu.

---

# 🚀 How to Run

## Step 1: Open the Project

Open the project folder in VS Code.

```powershell
cd "$HOME\Desktop\menu_application"
```

---

## Step 2: Run the Application

```powershell
python main.py
```

---

## Step 3: Login

Select:

```text
1
```

Use:

```text
Username: admin
Password: python123
```

---

# 🧪 Testing Scenarios

The following test cases can be used to verify the application.

| Test                    | Expected Result           |
| ----------------------- | ------------------------- |
| Correct login           | Login successful          |
| Incorrect password      | Login error               |
| Valid calculation       | Result displayed          |
| Non-numeric calculation | Error handled             |
| Division by zero        | Error handled             |
| Existing file           | File contents displayed   |
| Missing file            | Error logged              |
| Empty file              | Warning logged            |
| Write file              | File created successfully |
| Invalid menu choice     | Warning logged            |
| Logout                  | Session ended             |
| Unexpected error        | Critical log generated    |

---

# 💻 Sample Application Flow

```text
========================================
       MENU-DRIVEN APPLICATION
========================================
1. Login
2. Calculate
3. Read a File
4. Write a File
5. Logout
========================================

Enter your choice: 1

Enter username: admin
Enter password: python123

Login successful.
```

Then:

```text
Enter your choice: 2

Enter first number: 10
Enter second number: 20
Enter operator (+, -, *, /): +

Result: 30.0
```

Then:

```text
Enter your choice: 3

Enter file name: sample.txt

File Content:
Welcome to the Python logging project.
```

The application continues displaying the menu until the user selects:

```text
5. Logout
```

---

# 🧠 Key Concepts Demonstrated

## Modules

The application is divided into multiple modules:

```text
auth.py
calculator.py
file_operations.py
logger.py
exceptions.py
```

---

## Package

The `app` directory acts as the Python package:

```text
app/
├── __init__.py
├── auth.py
├── calculator.py
├── file_operations.py
├── logger.py
└── exceptions.py
```

---

## Exception Handling

Different types of errors are handled using:

```python
try:
    ...
except:
    ...
```

---

## Custom Exceptions

Application-specific exceptions are created using:

```python
class ApplicationError(Exception):
    pass
```

---

## Logging

The project uses Python's built-in:

```python
import logging
```

module to record application activity.

---

## File Handling

The project demonstrates reading and writing files using Python.

---

## Menu-Driven Application

A `while` loop keeps the application running:

```python
while True:
    display_menu()
```

The loop continues until the user chooses logout.

---

# 🏗️ Application Architecture

```text
                         main.py
                            │
                            ▼
                     Display Menu
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          auth.py      calculator.py   file_operations.py
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                        logger.py
                            │
                   ┌────────┴────────┐
                   ▼                 ▼
          application.log       error.log

                        exceptions.py
                              │
                              ▼
                     Custom Exceptions
```

---

# 🔑 Why Use Separate Modules?

Putting everything inside `main.py` would make the program difficult to read and maintain.

Instead:

```text
main.py
   ↓
Controls application

auth.py
   ↓
Handles authentication

calculator.py
   ↓
Handles calculations

file_operations.py
   ↓
Handles files

logger.py
   ↓
Handles logging

exceptions.py
   ↓
Handles custom errors
```

Each module has one clear responsibility.

---

# 🛠️ Technologies Used

* Python 3
* Python Standard Library
* `logging`
* `pathlib`
* Exception Handling
* Custom Exceptions
* File Handling
* Functions
* Modules
* Packages

No external packages are required.

---

# 🚀 Future Improvements

Possible improvements include:

* Store users in a database
* Password hashing
* Add more calculator operations
* Add file deletion and rename operations
* Add log rotation
* Add console logging
* Add timestamps and user IDs to logs
* Add unit tests
* Add configuration files
* Add a graphical user interface
* Add database logging
* Add command-line arguments

---

# 📌 Project Learning Summary

This project demonstrates how to build a structured Python application using:

```text
Functions
    ↓
Modules
    ↓
Packages
    ↓
Exception Handling
    ↓
Custom Exceptions
    ↓
File Handling
    ↓
Logging
    ↓
Multiple Log Handlers
    ↓
Menu-Driven Application
```

The primary learning objective is understanding **Python logging**, including how to generate different log levels and store application activity and errors in separate files.

The project also demonstrates an important real-world programming principle:

> **An error in one operation should be handled gracefully without terminating the entire application.**

---

## 👨‍💻 Author

**AI First**

> Learn AI. Build AI. Shape the Future.

---

## 📄 License

This project is created for **learning and educational purposes**.
