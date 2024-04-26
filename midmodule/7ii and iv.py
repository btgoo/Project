class Collection:
    def __init__(self):
        self.collection = []

    def make_student_collection(self, course_name):
        self.collection = {"course name": course_name, "students": []}

    def add_student(self, students):
        self.collection[students].append(students)

    def remove_student(self, students):
        self.collection[students].remove(students)

        def sort_students(self, students):
            self.collection[students].sort(key=get_student_name)

        def get_student(self, index):
            return self.collection[students][index]

        def get_student_name(self, students):
            return students["name"]