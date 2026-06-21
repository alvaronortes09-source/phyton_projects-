# Define a class called Faculty
class Faculty:
    def __init__(self, faculty_name):
        # Initialize the faculty with a name and empty lists of students and courses
        self.faculty_name = faculty_name  # Name of the faculty (string)
        self.students = []  # List of students in the faculty (list of Student objects)
        self.courses = []  # List of courses in the faculty (list of Course objects)

    # Methods for managing students in the faculty
    def add_student(self, student: Student):
        # Add a new student to the list of students in the faculty
        self.students.append(student)

    def remove_student(self, student: Student):
        # Remove a student from the list of students in the faculty if it exists
        if student in self.students:
            print(f"Student {student.name} has been removed")
            self.students.remove(student)
        else:
            print("This student is not in the faculty")

    def get_students(self, students: list):
        # Return the list of students in the faculty
        return self.students

    def get_courses(self, courses: list):
        # Return the list of courses in the faculty
        return self.courses

    # Methods for managing courses in the faculty
    def add_course(self, course: Course):
        # Add a new course to the list of courses in the faculty
        self.courses.append(course)

    def remove_course(self, course: Course):
        # Remove a course from the list of courses in the faculty if it exists
        if course in self.courses:
            print(f"Course {course.name} has been removed")
            self.courses.remove(course)
        else:
            print("This course is not in the faculty")

    # Methods for getting the number of students and courses
    def get_number_of_students(self, students: Students):
        # Return the number of students in the faculty
        return len(self.students)

    def get_number_of_courses(self, courses: Course):
        # Return the number of courses in the faculty
        return len(self.courses)

    # Import the csv library for exporting information to a CSV file
    import csv

    # Method for exporting student and course information to a CSV file
    def export_to_csv(self, filename='exported.csv'):
        # Open the file in write mode with the 'w' option (write)
        with open(filename, 'w', newline='') as csvfile:
            # Create a writer object to write to the CSV file
            writer = csv.writer(csvfile)

            # Write the header of the CSV file
            header = ['ID', 'Name', 'Course']
            writer.writerow(header)

            # Iterate over students and courses in the faculty and write to the CSV file
            for student in self.students:
                row = [student.id, student.name]
                for course in student.courses:
                    row.append(course)
                    writer.writerow(row)

def complete_report(self):
    # Iterate over students in the faculty and print their information
    for student in self.students:
        id_number = student.student_id  # ID number of the student (integer)
        name = student.name  # Name of the student (string)
        birth_date = student.birth_date  # Birth date of the student (string)
        print(f"ID Number = {id_number} | Name = {name} | Birth Date = {birth_date}")
        for course in student.courses:
            course_name = course.name  # Name of the course (string)
            credits = course.credit  # Credits of the course (integer)
            grade = course.grade  # Grade of the course (float)
            print(f"Course = {course_name} | Credits = {credits} | Grade = {grade}")

def statistics(self):
    # Get the total number of students
    total_students = len(self.students)

    # Get a list of grades from all students
    grades = []
    for student in self.students:
        for course in student.courses:
            grade = course.grade  # Grade of the course (float)
            grades.append(grade)

    # Calculate the average grade
    average_grade = sum(grades) / total_students

    # Initialize counters for students who passed and failed
    passed_students = 0
    failed_students = 0

    # Iterate over students in the faculty and check if they passed or failed
    for student in self.students:
        for course in student.courses:
            grade = course.grade  # Grade of the course (float)
            if grade >= 5:  # Check if the student passed (grade >= 5)
                passed_students += 1
            else:
                failed_students += 1

    # Print statistics
    print(f"Total Number of Students: {total_students}")
    print(f"Number of Students Who Passed: {passed_students}")
    print(f"Number of Students Who Failed: {failed_students}")

