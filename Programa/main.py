# ======================================================
# MAIN FILE - STUDENT MANAGEMENT SYSTEM
# ======================================================

# Visual separator used to improve console readability
SPACE = "                                                            "
SEPARATOR = "----------------------------------------------------------"

# Import project classes
from course import Course
from student import Student
from faculty import Faculty
from faculty import complete_report

# ======================================================
# SAMPLE DATA
# ======================================================

# Create the initial list of students
students = []

# Create the available courses
courses = [
    Course("Mathematics", 5, 0),
    Course("Physics", 5, 0),
    Course("Chemistry", 5, 0),
    Course("Biology", 4, 0),
    Course("History", 4, 0),
    Course("Geography", 4, 0),
    Course("Philosophy", 3, 0),
    Course("Psychology", 3, 0),
    Course("Sociology", 3, 0)
]


# Assign every course to every sample student


# Create faculties
faculties = [
    Faculty("Science Faculty"),
    Faculty("Humanities Faculty"),
    Faculty("Engineering Faculty"),
    Faculty("Arts Faculty"),
    Faculty("Business Faculty")
]
# Populate each faculty with sample students



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
    print("6. Statistics")
    print("7. Exit")

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
    if option not in (1, 2, 3, 4, 5, 6,7):
        print("Invalid option.")
        continue

    # ==================================================
    # OPTION 1 - SHOW STUDENTS
    # ==================================================

    if option == 1:

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
        complete_report(selected_faculty)

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
            print(f"{i + 1}. {course.course_name}")

        selection = int(input("Enter the course number: "))

        # Validate course selection
        if 1 <= selection <= len(courses):
            selected_course = courses[selection - 1]
        else:
            print("Invalid number")
            continue

        # Create a NEW course object for this student
        new_course = Course(
            selected_course.course_name,
            selected_course.credits,
            0
)

        # Add the new course to the student
        selected_student.add_course(new_course)

        # Ask for the student's grade
        selected_student.update_grade(new_course.course_name)

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
        for i, student in enumerate(selected_faculty.faculty_students):
            print(f"{i + 1}. {student.name}")

        selection = int(input("Enter the student number: "))

        # Validate student selection
        if 1 <= selection <= len(selected_faculty.faculty_students):
            selected_student = selected_faculty.faculty_students[selection - 1]
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
        for i, course in enumerate(student.courses_taken):
            print(f"{i + 1}. {course.course_name}")

        selection = int(input("Enter the course number: "))

        # Validate course selection
        if 1 <= selection <= len(student.courses_taken):
            selected_course = courses[selection - 1]
        else:
            print("Invalid number")
            continue

        # Remove the course
        selected_student.remove_course(selected_course)

        print("Course removed successfully.")

    # ==================================================
    # OPTION 6 - Statistics
    # ==================================================
    elif option == 6:
        
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
        Faculty.statistics(selected_faculty)
        
    # ==================================================
    # OPTION 7 - EXIT
    # ==================================================
    elif option == 7:
        print(SEPARATOR)
        print("THANKS FOR USING THE STUDENT MANAGEMENT SYSTEM")
        print(SEPARATOR)
        break