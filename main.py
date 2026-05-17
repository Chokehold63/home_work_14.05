class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and  0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += [grade]

        if len(all_grades) == 0:
            return 0

        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += [grade]

        if len(all_grades) == 0:
            return 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.average_grade()}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')


student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# print(student.rate_lecture(lecturer, 'Python', 7))  # None
# print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
# print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
# print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
#
# print(lecturer.grades)  # {'Python': [7]}

print(reviewer)
print(lecturer)
print(student)