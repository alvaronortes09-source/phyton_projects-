# ======================================================
# MAIN FILE - STUDENT MANAGEMENT SYSTEM
# ======================================================

# Visual separator used to improve console readability
SEPARATOR = "----------------------------------------------------------"

# Import project classes
from course import Course
from student import Student
from faculty import Faculty

# ======================================================
# SAMPLE DATA
# ======================================================

# Create the initial list of students
students = [
    Student(1, "Juan Pérez", "1990-01-01"),
    Student(2, "María Gómez", "1992-06-15"),
    Student(3, "Carlos Díaz", "1988-03-20"),
    Student(4, "Sofía García", "1995-09-12"),
    Student(5, "Daniel Rodríguez", "1990-11-25")
]

# Create the available courses
courses = [
    Course("Mathematics", 4, 8),
    Course("Physics", 3, 7),
    Course("Chemistry", 3, 6),
    Course("Biology", 4, 9),
    Course("History", 2, 5)
]

# Assign every course to every sample student
for student in students:
    for course in courses:
        student.add_course(course)

# Create faculties
faculties = [
    Faculty("Science Faculty"),
    Faculty("Humanities Faculty")
]

# Populate each faculty with sample students
for faculty in faculties:

    for i in range(5):

        new_student = Student(
            i + 1,
            f"Student {i + 1}",
            "1990-01-01"
        )

        # Give every sample student one course
        new_student.add_course(courses[0])

        faculty.add_student(new_student)

# ======================================================
# MAIN MENU
# ======================================================

def main_menu():

    print(SEPARATOR)
    print("MAIN MENU")
    print(SEPARATOR)

    print("1. Show students")
    print("2. Add student")
    print("3. Add course")
    print("4. Remove student")
    print("5. Remove course")
    print("6. Exit")

    print(SEPARATOR)


# ======================================================
# MAIN PROGRAM
# ======================================================

while True:

    # Display the menu every iteration
    main_menu()

    # Validate that the user enters a number
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Validate menu option
    if option not in (1, 2, 3, 4, 5, 6):
        print("Invalid option.")
        continue

    # ==================================================
    # OPTION 1 - SHOW STUDENTS
    # ==================================================

    if option == 1:

        for faculty in faculties:

            print(f"\n{faculty.faculty_name}")

            for student in faculty.students:

                print(student)

                # Display every course assigned to the student
                for course in student.courses_taken:
                    print(f"   - {course}")

    # ==================================================
    # OPTION 2 - ADD STUDENT
    # ==================================================

    elif option == 2:

        print("Select a faculty")

        # Display every faculty
        for i, faculty in enumerate(faculties):
            print(f"{i + 1}. {faculty.faculty_name}")

        selection = int(input("Enter the faculty number: "))

        # Validate faculty selection
        if 1 <= selection <= len(faculties):
            selected_faculty = faculties[selection - 1]
        else:
            print("Invalid number")
            continue

        # Ask for the student's name
        new_student_name = input("Student name: ")

        # Generate a new ID
        new_student_id = len(students) + 1

        # Create the student
        new_student = Student(
            new_student_id,
            new_student_name,
            "1990-01-01"
        )

        # Store the student globally
        students.append(new_student)

        # Add the student to the selected faculty
        selected_faculty.add_student(new_student)

        print("Student added successfully.")

    # ==================================================
    # OPTION 3 - ADD COURSE
    # ==================================================

    elif option == 3:

        print("Select a student")

        # Display every student
        for i, student in enumerate(students):
            print(f"{i + 1}. {student.name}")

        selection = int(input("Enter the student number: "))

        # Validate student selection
        if 1 <= selection <= len(students):
            selected_student = students[selection - 1]
        else:
            print("Invalid number")
            continue

        print("Select a course")

        # Display every available course
        for i, course in enumerate(courses):
            print(f"{i + 1}. {course.name}")

        selection = int(input("Enter the course number: "))

        # Validate course selection
        if 1 <= selection <= len(courses):
            selected_course = courses[selection - 1]
        else:
            print("Invalid number")
            continue

        # Add the selected course
        selected_student.add_course(selected_course)

        print("Course assigned successfully.")

    # ==================================================
    # OPTION 4 - REMOVE STUDENT
    # ==================================================

    elif option == 4:

        print("Select a faculty")

        # Display every faculty
        for i, faculty in enumerate(faculties):
            print(f"{i + 1}. {faculty.faculty_name}")

        selection = int(input("Enter the faculty number: "))

        # Validate faculty selection
        if 1 <= selection <= len(faculties):
            selected_faculty = faculties[selection - 1]
        else:
            print("Invalid number")
            continue

        print("Select a student")

        # Display only students from the selected faculty
        for i, student in enumerate(selected_faculty.students):
            print(f"{i + 1}. {student.name}")

        selection = int(input("Enter the student number: "))

        # Validate student selection
        if 1 <= selection <= len(selected_faculty.students):
            selected_student = selected_faculty.students[selection - 1]
        else:
            print("Invalid number")
            continue

        # Remove the student
        selected_faculty.remove_student(selected_student)

        print("Student removed successfully.")

    # ==================================================
    # OPTION 5 - REMOVE COURSE
    # ==================================================

    elif option == 5:

        print("Select a student")

        # Display every student
        for i, student in enumerate(students):
            print(f"{i + 1}. {student.name}")

        selection = int(input("Enter the student number: "))

        # Validate student selection
        if 1 <= selection <= len(students):
            selected_student = students[selection - 1]
        else:
            print("Invalid number")
            continue

        print("Select a course")

        # Display every course
        for i, course in enumerate(courses):
            print(f"{i + 1}. {course.name}")

        selection = int(input("Enter the course number: "))

        # Validate course selection
        if 1 <= selection <= len(courses):
            selected_course = courses[selection - 1]
        else:
            print("Invalid number")
            continue

        # Remove the course
        selected_student.remove_course(selected_course)

        print("Course removed successfully.")

    # ==================================================
    # OPTION 6 - EXIT
    # ==================================================

    elif option == 6:

        print("Thank you for using the Student Management System.")
        break