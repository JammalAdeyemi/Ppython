class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def __init__(self, name, duration, location):
        self.name = name
        self.duration = duration
        self.location = location  
    # Add another method in the Course class that prints the head office location: Cape Town
    def get_head_office(self):
        print(f"Head office location: {self.location}")

    def contact_details(self):
        print(f"Please contact us by visiting {self.contact_website}")

# Create a subclass called OOPCourse that inherits from the Course class
class OOPCourse(Course):
    # Add the description and trainer attributes to the constructor
    def __init__(self, name, duration, location, description, trainer):
        super().__init__(name, duration, location)
        self.description = description
        self.trainer = trainer
        self.course_id = "#12345"
    # Create a method in the subclass named "trainer_details" that prints what the course is about and the name of the trainer by using the description and trainer attributes.
    def trainer_details(self):
        print(f"This course is about {self.description} and the trainer is {self.trainer}")
    # Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
    def show_course_id(self):
        print(f"ID number of the course: {self.course_id}")

course_1 = OOPCourse("Fundamentals of Computer Science", "3 months", "Cape Town", "OOP Fundamentals", "Mr Anon A. Mouse")

course_1.get_head_office()
course_1.trainer_details()
course_1.show_course_id()
    
