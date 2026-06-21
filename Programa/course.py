# Define a class called Course to represent a course
class Course:
    # Initialize the attributes of the class when an instance is created
    def __init__(self, course_name: str, credits: int, grade: float):
        # Assign the provided values to the corresponding attributes
        self.course_name = course_name  # Name of the course (string)
        self.credits = credits  # Credits of the course (integer)
        self.grade = grade  # Grade obtained in the course (float)

    # Define a method to return a string representation of the class instance
    def __str__(self):
        # Return a formatted string with the course information
        return f"Course: {self.course_name} | Credits: {self.credits} | Grade: {self.grade}"
