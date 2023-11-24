# Задание 1
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
# Задание 2 и 3
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades) if self.grades else 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses) if self.finished_courses else 'отсутствуют'
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\n"
               f"Курсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}\n")


# Задание 4
best_student = Student('Максим', 'Емельянов', 'мужской')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

another_student = Student('Алиса', 'Хрованская', 'женский')
another_student.courses_in_progress += ['Python']

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}\n")

# Задание 4
cool_lecturer = Lecturer('Сергей', 'Новиков')
cool_lecturer.courses_attached += ['Python']

another_cool_lecturer = Lecturer('Станислав', 'Борский')
another_cool_lecturer.courses_attached += ['Python']

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Задание 4
cool_mentor = Reviewer('Николай', 'Ковалев')
cool_mentor.courses_attached += ['Python']

another_cool_mentor = Reviewer('Федор', 'Сапрыкин')
another_cool_mentor.courses_attached += ['Python']

# Оценки студентов и лекторов
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)

best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 7)

another_cool_mentor.rate_hw(another_student, 'Python', 9)
another_cool_mentor.rate_hw(another_student, 'Python', 8)

another_student.rate_lecture(another_cool_lecturer, 'Python', 9)
another_student.rate_lecture(another_cool_lecturer, 'Python', 8)

# Вывод результатов
print(best_student)
print(another_student)
print(cool_lecturer)
print(another_cool_lecturer)