# 🎓 Student Management System

## Introduction

The **Student Management System** is a console-based application developed in **Python** using **Object-Oriented Programming (OOP)** principles.

The goal of the project is to simulate how a university or educational institution manages its students, faculties, and courses. Instead of storing information in simple variables or lists, the application models real-world entities as objects, making the code easier to understand, maintain, and extend.

This project was developed as a practical exercise to improve software design skills, understand relationships between classes, and apply object-oriented concepts in a real application.

---

# How the System Works

The application is entirely menu-driven and runs from the terminal.

When the program starts, the user is presented with a menu that allows different management operations. Each option performs a specific task by interacting with the underlying classes.

The general workflow is the following:

1. The user selects an option from the main menu.
2. The program validates the user's input.
3. The corresponding objects are located or created.
4. The requested operation is executed.
5. The updated information is displayed to the user.

Every operation is performed using object methods instead of manipulating data directly, following good Object-Oriented Programming practices.

---

# Software Design

The system is organized around three main classes that represent the most important entities of an academic environment.

## Student

A `Student` object represents a single student.

Each student stores personal information such as:

* Student ID
* Name
* Birth date

Additionally, every student owns a personal list of enrolled courses.

The student class is responsible for operations such as:

* Enrolling in a course
* Removing a course
* Updating grades
* Displaying student information

This design ensures that each student manages their own academic record independently.

---

## Course

A `Course` object represents a university subject.

Each course stores:

* Course name
* Number of credits
* Grade obtained by the student

An important design decision is that **every student receives their own independent copy of a course**.

This means that two different students enrolled in Mathematics can have completely different grades without affecting each other.

This approach avoids shared state between students and accurately models real-world academic records.

---

## Faculty

A `Faculty` object groups multiple students.

Instead of containing academic information directly, a faculty acts as an administrator for its students.

Its responsibilities include:

* Adding students
* Removing students
* Generating reports
* Calculating statistics
* Exporting data to CSV files

This separation of responsibilities keeps the project organized and follows the principle that each class should have a clear and specific purpose.

---

# Programming Approach

The project follows an object-oriented architecture where each class has clearly defined responsibilities.

Rather than writing all the logic inside a single file, the program is divided into multiple modules, making the code easier to read, reuse, and maintain.

Input validation is performed throughout the application to prevent invalid data from crashing the program. User selections are checked before executing operations, and exception handling is used whenever numeric input is required.

Overall, the project demonstrates how Object-Oriented Programming can be used to model real-world systems while keeping the code modular, scalable, and easy to understand.
