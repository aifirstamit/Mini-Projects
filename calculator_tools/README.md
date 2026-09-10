# 🧮 Build Your Own `calculator_tools` Python Package

## 📌 Project Overview

This project demonstrates how to create a **reusable Python package** instead of putting all functionality into one Python file.

The package is named:

```text
calculator_tools
```

It contains multiple Python modules for:

* Basic arithmetic operations
* Percentage calculation
* Average calculation
* Temperature conversion
* Unit conversion
* Custom exception handling
* Error handling
* Package imports

The main goal of this project is to understand the difference between a:

> **Function → Module → Package → Import**

---

# 🎯 Project Objective

The objective of this project is to build a reusable Python package that provides functions for:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Percentage calculation
6. Average calculation
7. Celsius to Fahrenheit conversion
8. Fahrenheit to Celsius conversion
9. Kilometers to miles conversion
10. Miles to kilometers conversion

The project also handles errors such as:

* Division by zero
* Invalid values
* Incorrect data types
* Empty lists
* Negative values where not allowed
* Unsupported operations

A custom exception called:

```python
InvalidOperationError
```

has also been created.

---

# 📁 Project Structure

```text
calculator_tools/
│
├── __init__.py
├── arithmetic.py
├── statistics.py
├── converter.py
├── exceptions.py
└── main.py
```

---

# 📄 File Description

## 1. `__init__.py`

This file initializes the `calculator_tools` package.

It imports the functions from the different modules so they can be accessed directly from the package.

Example:

```python
from calculator_tools import add
```

---

## 2. `arithmetic.py`

This module contains mathematical operations.

Functions included:

```text
add()
subtract()
multiply()
divide()
calculate_percentage()
calculate_operation()
```

It also performs data validation and raises appropriate errors.

---

## 3. `statistics.py`

This module contains statistical functionality.

Function included:

```text
calculate_average()
```

The average is calculated using a loop instead of Python's built-in `sum()` function.

---

## 4. `converter.py`

This module contains conversion functions.

Functions included:

```text
celsius_to_fahrenheit()
fahrenheit_to_celsius()
kilometers_to_miles()
miles_to_kilometers()
```

---

## 5. `exceptions.py`

This module contains the custom exception:

```python
InvalidOperationError
```

It is used when the user requests an operation that the package does not support.

---

## 6. `main.py`

This is the demonstration program.

It imports functionality from the `calculator_tools` package and demonstrates:

* Arithmetic
* Percentage
* Average
* Temperature conversion
* Unit conversion
* Operation selection
* Error handling

---

# 🧠 Understanding Function, Module, Package and Import

This is the most important concept of this project.

## Function

A function is a reusable block of code that performs a specific task.

Example:

```python
def add(a, b):
    return a + b
```

Here:

```text
add()
```

is a function.

---

## Module

A module is a Python file containing related code.

For example:

```text
arithmetic.py
```

is a module containing arithmetic functions.

---

## Package

A package is a folder containing related Python modules.

In this project:

```text
calculator_tools/
```

is the package.

---

## Import

Import allows us to use code from another module or package.

Example:

```python
from calculator_tools import add
```

This allows `main.py` to use the `add()` function.

---

# 🔢 Functionality Demonstrated

## 1. Addition

```python
add(10, 20)
```

Output:

```text
30
```

---

## 2. Subtraction

```python
subtract(20, 10)
```

Output:

```text
10
```

---

## 3. Multiplication

```python
multiply(10, 5)
```

Output:

```text
50
```

---

## 4. Division

```python
divide(20, 5)
```

Output:

```text
4.0
```

The program also prevents division by zero.

Example:

```python
divide(10, 0)
```

Output:

```text
Error: Cannot divide by zero.
```

---

# 📊 Percentage Calculation

The package provides:

```python
calculate_percentage(500, 20)
```

Output:

```text
100.0
```

This means:

```text
20% of 500 = 100
```

### 💡 Real-Life Example

Percentage calculations are commonly used for:

* Discounts
* Marks
* Sales growth
* Tax calculations
* Business reports

---

# 📈 Average Calculation

The package provides:

```python
numbers = [10, 20, 30, 40, 50]

calculate_average(numbers)
```

Output:

```text
30.0
```

The function uses a loop to calculate the total and then divides it by the number of values.

### 💡 Data Science Connection

Average is one of the most commonly used concepts in data analysis.

For example:

```text
Student Marks
↓
Calculate Average
↓
Understand Student Performance
```

It is also used when analyzing:

* Customer spending
* Employee salaries
* Product prices
* Temperature data
* Machine-learning datasets

---

# 🌡️ Temperature Conversion

The package supports:

### Celsius → Fahrenheit

```python
celsius_to_fahrenheit(25)
```

Output:

```text
77.0
```

### Fahrenheit → Celsius

```python
fahrenheit_to_celsius(77)
```

Output:

```text
25.0
```

---

# 📏 Unit Conversion

The package supports:

### Kilometers → Miles

```python
kilometers_to_miles(10)
```

Output:

```text
6.21371
```

### Miles → Kilometers

```python
miles_to_kilometers(10)
```

Output:

```text
16.0934
```

---

# ⚠️ Error Handling

Error handling is an important part of this project.

The package handles different types of errors.

## 1. Division by Zero

Example:

```python
divide(10, 0)
```

Output:

```text
Error: Cannot divide by zero.
```

---

## 2. Incorrect Data Type

Example:

```python
add(10, "20")
```

Output:

```text
Error: Second value must be a number.
```

---

## 3. Empty List

Example:

```python
calculate_average([])
```

Output:

```text
Error: Cannot calculate average of an empty list.
```

---

## 4. Unsupported Operation

Example:

```python
calculate_operation("power", 10, 2)
```

Output:

```text
Error: Unsupported operation: power
```

This error uses the custom:

```python
InvalidOperationError
```

---

# 🛠️ Custom Exception

A custom exception was created:

```python
class InvalidOperationError(Exception):
    """Raised when an unsupported operation is requested."""
    pass
```

This allows the program to clearly identify unsupported calculator operations.

Example:

```python
try:
    calculate_operation("power", 10, 2)

except InvalidOperationError as error:
    print("Error:", error)
```

---

# ▶️ How to Run the Project

## Step 1: Open the project folder

The project is located on the Desktop:

```text
C:\Users\Data Science\Desktop\calculator_tools
```

---

## Step 2: Open the parent folder in the terminal

Go to:

```text
C:\Users\Data Science\Desktop
```

PowerShell:

```powershell
cd "C:\Users\Data Science\Desktop"
```

---

## Step 3: Run the package

Use:

```powershell
python -m calculator_tools.main
```

### Why use `-m`?

The `-m` option tells Python to run `main` as a module inside the `calculator_tools` package.

This is important because this project is specifically demonstrating **Python packages and modules**.

---

# 🖥️ Sample Output

```text
===== Arithmetic Operations =====
Addition: 30
Subtraction: 10
Multiplication: 50
Division: 4.0

===== Percentage =====
20% of 500: 100.0

===== Average =====
Numbers: [10, 20, 30, 40, 50]
Average: 30.0

===== Temperature Conversion =====
25 Celsius to Fahrenheit: 77.0
77 Fahrenheit to Celsius: 25.0

===== Unit Conversion =====
10 Kilometers to Miles: 6.21371
10 Miles to Kilometers: 16.0934

===== Operation Selection =====
Add: 150
Multiply: 50

===== Error Handling =====
Error: Cannot divide by zero.
Error: Second value must be a number.
Error: Cannot calculate average of an empty list.
Error: Unsupported operation: power
```

---

# 🧪 Testing

The following test cases were performed.

| Test                  | Input              | Expected Result | Status |
| --------------------- | ------------------ | --------------- | ------ |
| Addition              | `10, 20`           | `30`            | ✅      |
| Subtraction           | `20, 10`           | `10`            | ✅      |
| Multiplication        | `10, 5`            | `50`            | ✅      |
| Division              | `20, 5`            | `4.0`           | ✅      |
| Division by zero      | `10, 0`            | Error           | ✅      |
| Percentage            | `500, 20`          | `100.0`         | ✅      |
| Average               | `[10,20,30,40,50]` | `30.0`          | ✅      |
| Empty average         | `[]`               | Error           | ✅      |
| Celsius conversion    | `25`               | `77.0°F`        | ✅      |
| Fahrenheit conversion | `77`               | `25.0°C`        | ✅      |
| Kilometer conversion  | `10`               | `6.21371 miles` | ✅      |
| Unsupported operation | `"power"`          | Custom error    | ✅      |

---

# 💻 Technologies Used

* Python 3
* Python Functions
* Python Modules
* Python Packages
* Import Statements
* Exception Handling
* Custom Exceptions
* Lists
* Loops
* Conditional Statements

No external Python libraries are required.

---

# 📦 Requirements

This project uses only the Python standard library.

Therefore, no external packages are required.

`requirements.txt` can remain empty.

---

# 🎯 Why Packages Are Useful

Imagine a large Data Science project containing hundreds of functions.

Putting everything into one file would make the project:

* Difficult to understand
* Difficult to test
* Difficult to maintain
* Difficult to reuse

Instead, we can organize code into modules and packages.

For example:

```text
Data Science Project
│
├── data_processing.py
├── statistics.py
├── visualization.py
├── machine_learning.py
└── utilities/
```

This makes the project easier to manage.

---

# 🤖 Data Science & AI Connection

Python packages are heavily used in Data Science and Artificial Intelligence.

Examples include:

```text
NumPy
Pandas
Matplotlib
Scikit-learn
TensorFlow
PyTorch
```

These are large collections of reusable Python code organized into modules and packages.

For example, instead of writing mathematical functionality from scratch, a Data Scientist can import a library and reuse existing functionality.

This project gives a basic understanding of how such reusable Python structures are organized.

---

# 🧠 What I Learned

Through this project, I learned:

* What a function is
* What a module is
* What a package is
* How `__init__.py` works
* How imports work
* How to organize Python code
* How to create reusable functions
* How to create custom exceptions
* How to handle errors
* How to validate input values
* How to run a Python package using `python -m`
* Why modular programming is useful

---

# ⭐ Important Concepts

### Function

```text
A function is a reusable block of code.

def add(a, b):
    return a + b
```

### Module

```text
A module is a Python .py file containing related code.

arithmetic.py

contains arithmetic functions.
```

### Package

```text
A package is a folder containing related Python modules.

calculator_tools/

is your package.
```

### Import

```text
import allows us to use code from another module/package.

from calculator_tools import add
```

### Exception

```text
An error that occurs during program execution
```

### Custom Exception

```text
An exception created by the programmer
```

---

# 🚧 Errors and Challenges

One important challenge during this project was understanding how Python identifies a package.

Running:

```powershell
python calculator_tools/main.py
```

from the parent directory can cause package import issues because the file is being executed directly.

The correct package-oriented approach is:

```powershell
python -m calculator_tools.main
```

This helped me understand the difference between running a Python file directly and running a module as part of a package.

---


## 🚀 Final Takeaway

> **Functions help us reuse logic.**
>
> **Modules help us organize functions.**
>
> **Packages help us organize modules.**
>
> **Imports help us reuse that organized code.**

This project provides the foundation for understanding how larger Python libraries used in **Data Science and AI** are structured.

---

### 📌 Project

**Project Name:** `calculator_tools`

**Language:** Python

**Focus:** Functions, Modules, Packages, Imports & Exception Handling

**YouTube Channel:** AI First

Please subscribe to my YouTube channel: https://www.youtube.com/@aifirstamit
