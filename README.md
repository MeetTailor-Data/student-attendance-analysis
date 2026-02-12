# Student Attendance Analysis Using NumPy (Python)

## Project Description

The Student Attendance Analysis project is a Python application that uses the NumPy library to analyze student attendance data.
The program calculates total present days, total absent days, attendance percentage, exam eligibility status, and identifies the specific days the student was absent.

This project demonstrates basic data analysis using NumPy arrays and is suitable for beginners learning numerical computing in Python.

The application executes once and displays all computed results in the terminal.

---

## Features

* Store attendance data using NumPy arrays
* Calculate total present days
* Calculate total absent days
* Compute attendance percentage
* Determine exam eligibility based on percentage
* Identify absent day indices
* Simple terminal-based output

---

## Concepts Used

### Python Fundamentals

* Lists
* Variables
* Data types (int, float)
* Input and output formatting

### NumPy Concepts

* NumPy arrays
* Aggregation functions (sum)
* Conditional selection
* Index filtering using where()

### Programming Concepts

* Percentage calculation
* Conditional eligibility checking
* Array-based data analysis
* Logical decision making

---

## Project Structure

```
student-attendance-analysis/
│
├── attendance_analysis.py
└── README.md
```

---

## How to Run the Program

### Requirements

* Python 3.x installed on the system
* NumPy library installed

### Steps

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the following command:

```
python attendance_analysis.py
```

---

## Evaluation Criteria

* Attendance Percentage ≥ 75 : Eligible for Exam
* Attendance Percentage < 75 : Not Eligible for Exam

---

## Sample Output

```
Total Present Days: 20
Total Absent Days: 10
Attendance Percentage: 66.67%
Student is Not Eligible For Exam
Days Student is Absent: [1 4 8 10 13 16 21 24 27]
```

---

## Edge Cases Handled

* Accurate attendance percentage calculation
* Correct identification of absent days
* Proper eligibility decision based on percentage

---

## Author

Meet Tailor

Python Programming Learner

---

## License

This project is created for learning and educational purposes only.

---

## Project Status

Completed

Last Updates: 2026
