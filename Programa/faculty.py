# Visual separator used to improve console readability
SPACE = "                                                            "
SEPARATOR = "----------------------------------------------------------"

# Define a class called Faculty
class Faculty:
    def __init__(self, faculty_name):
        # Initialize the faculty with a name and empty lists of students and courses
        self.faculty_name = faculty_name  # Name of the faculty (string)
        self.faculty_students = []  # List of students in the faculty (list of Student objects)

    # Methods for managing students in the faculty
    def add_student(self, student: Student):
        # Add a new student to the list of students in the faculty
        self.faculty_students.append(student)

    def remove_student(self, student: Student):
        # Remove a student from the list of students in the faculty if it exists
        if student in self.faculty_students:
            print(f"Student {student.name} has been removed")
            self.faculty_students.remove(student)
        else:
            print("This student is not in the faculty")
    
    def statistics(self):

        # Total number of students
        total_students = len(self.faculty_students)

        # Store every grade
        grades = []

        for student in self.faculty_students:
            for course in student.courses_taken:
                grades.append(course.grade)

        # Calculate the average grade
        if len(grades) > 0:
            average_grade = sum(grades) / len(grades)
        else:
            average_grade = 0

        # Count passed and failed courses
        passed_courses = 0
        failed_courses = 0

        for student in self.faculty_students:
            for course in student.courses_taken:

                if course.grade >= 5:
                    passed_courses += 1
                else:
                    failed_courses += 1

        print(SPACE)
        print(SEPARATOR)
        print(f"Total students: {total_students}")
        print(f"Passed courses: {passed_courses}")
        print(f"Failed courses: {failed_courses}")
        print(f"Average grade: {average_grade:.2f}")
        print(SEPARATOR)
        print(SPACE)
        

def complete_report(self,):
    # Iterate over students in the faculty and print their information
    for student in self.faculty_students:
        id_number = student.student_id  # ID number of the student (integer)
        name = student.name  # Name of the student (string)
        birth_date = student.birth_date  # Birth date of the student (string)
        print(f"ID Number = {id_number} | Name = {name} | Birth Date = {birth_date}")
        for course in student.courses_taken:
            course_name = course.course_name  # Name of the course (string)
            credits = course.credits  # Credits of the course (integer)
            grade = course.grade  # Grade of the course (float)
            print(f"Course = {course_name} | Credits = {credits} | Grade = {grade}")