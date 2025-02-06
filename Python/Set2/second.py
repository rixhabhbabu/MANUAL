class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)
            print(f"{self.name} enrolled in {course.name}")
        else:
            print(f"{self.name} is already enrolled in {course.name}")

    def drop_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            course.remove_student(self)
            print(f"{self.name} dropped {course.name}")
        else:
            print(f"{self.name} is not enrolled in {course.name}")

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:")
        for course in self.enrolled_courses:
            print(f" - {course.name}")

class Teacher:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.courses_teaching = []

    def assign_to_course(self, course):
        if course not in self.courses_teaching:
            self.courses_teaching.append(course)
            course.assign_teacher(self)
            print(f"{self.name} assigned to teach {course.name}")
        else:
            print(f"{self.name} is already teaching {course.name}")

    def remove_from_course(self, course):
        if course in self.courses_teaching:
            self.courses_teaching.remove(course)
            course.remove_teacher()
            print(f"{self.name} removed from teaching {course.name}")
        else:
            print(f"{self.name} is not teaching {course.name}")

    def display_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Teacher ID: {self.teacher_id}")
        print("Courses Teaching:")
        for course in self.courses_teaching:
            print(f" - {course.name}")

class Course:
    def __init__(self, course_code, name):
        self.course_code = course_code
        self.name = name
        self.students = []
        self.teacher = None

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
        else:
            print(f"{student.name} is already in the course.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"{student.name} is not in the course.")

    def assign_teacher(self, teacher):
        if self.teacher is not None:
            print(f"{self.teacher.name} is already assigned to this course. Removing them first.")
            self.teacher.courses_teaching.remove(self)
        self.teacher = teacher
        if self not in teacher.courses_teaching:
            teacher.courses_teaching.append(self)

    def remove_teacher(self):
        if self.teacher:
            self.teacher.courses_teaching.remove(self)
            self.teacher = None
        else:
            print("No teacher assigned to this course.")

    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.name}")
        if self.teacher:
            print(f"Assigned Teacher: {self.teacher.name}")
        else:
            print("Assigned Teacher: None")
        print("Enrolled Students:")
        for student in self.students:
            print(f" - {student.name}")

# Example usage
if __name__ == "__main__":
    # Create courses
    math101 = Course("MATH101", "Introduction to Mathematics")
    physics201 = Course("PHYS201", "Advanced Physics")

    # Create students
    alice = Student("Alice", "S12345")
    bob = Student("Bob", "S67890")

    # Create teachers
    mr_smith = Teacher("Mr. Smith", "T98765")
    mrs_jones = Teacher("Mrs. Jones", "T54321")

    # Enroll students in courses
    alice.enroll_in_course(math101)
    alice.enroll_in_course(physics201)
    bob.enroll_in_course(math101)

    # Assign teachers to courses
    mr_smith.assign_to_course(math101)
    mrs_jones.assign_to_course(physics201)

    # Display information
    print("\n--- Course Information ---")
    math101.display_info()
    print("\n")
    physics201.display_info()

    print("\n--- Student Information ---")
    alice.display_info()
    print("\n")
    bob.display_info()

    print("\n--- Teacher Information ---")
    mr_smith.display_info()
    print("\n")
    mrs_jones.display_info()

    # Drop a course
    alice.drop_course(math101)
    print("\n--- After Dropping a Course ---")
    math101.display_info()
    #Hehe My name is Rishabh babu and i Make chnge in this file from my local machine and By git bash