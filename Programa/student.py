# Define a class called Student to represent a student
class Student:
    # Initialize the attributes of the class when an instance is created
    def __init__(self, student_id: int, name: str, birth_date: str):
        # Assign the provided values to the corresponding attributes
        self.student_id = student_id  # ID of the student (integer)
        self.name = name  # Name of the student (string)
        self.birth_date = birth_date  # Birth date of the student (string)

        # Initialize an empty list to store courses taken by the student
        self.courses_taken = []

    # Define a method to return a string representation of the class instance
    def __str__(self):
        # Return a formatted string with the student information
        return f"ID: {self.student_id} | Name: {self.name} | Birth Date: {self.birth_date}"

    # Define a method to add a course taken by the student
    def add_course(self, course: Course):
        # Add the provided course to the list of courses taken by the student
        if course not in self.courses_taken:
            self.courses_taken.append(course)
        else:
            print("That course is currently added")

    # Define a method to add a course taken by the student
    def remove_course(self, course: Course):
        # Add the provided course to the list of courses taken by the student
        if course not in self.courses_taken:
            print("The student is not enrolled in this course.")
        else:
            self.courses_taken.remove(course)
            
    # Define a method to update the grade of a specific course taken by the student
    def update_grade(self, course_name: Course,):
        # Iterate over each course in the list of courses taken by the student
        for current_course in self.courses_taken:
            if current_course.course_name == course_name:  # Check if the course name matches
                new_grade = int(input("Enter the new grade: "))
                current_course.grade = new_grade
                print("New grade added succesfully")

        # If no matching course is found, print a message to indicate that
        else:
            print("Student has not taken this course")
