class Mentor:
   def __init__(self, name, surname): 
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    def grading(self, student, course):
        if isinstance(student, Student) and course in self.courses_attached:
            student.grades[course]= 5
        else:
            print('Ошибка')

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, score):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            lecturer.grades[course] = score
        else:
            print('Ошибка')



lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

reviewer.grading(student, 'C++')
reviewer.grading(student, 'Java')
print(student.grades)
print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
print(lecturer.grades)  # {'Python': [7]}  