class MyClass:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def calculate_average(students, course_name):
    total = 0
    for student in students:
        total += student.grade
    average_grade = total / len(students)
    print(f"Средняя оценка для курса {course_name} - {average_grade}")

students = [Student("Алена", 85), Student("Иван", 90), Student("Николай", 80)]
calculate_average(students, "Python")
