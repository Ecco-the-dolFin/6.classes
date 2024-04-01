class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_w(self, lecturer, course, grade):
        if grade > 10 or grade < 1:
            return 'Неверная оценка'

        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades += grades

        if len(total_grades) == 0:
            return 'Нет оценок'

        return sum(total_grades) / len(total_grades)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.get_average_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades += grades
        return sum(total_grades) / len(total_grades)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.get_average_grade()}')

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}, surname: {self.surname}'


def get_average_grade_student(students_list, course_name):
    avg_grades = []
    for student in students_list:
        if course_name in student.grades:
            avg_grades += student.grades[course_name]

    if len(avg_grades) == 0:
        return 'Нет оценок'

    return sum(avg_grades) / len(avg_grades)


def get_average_grade_lecturers(lecturers_list, course_name):
    average_grades_lecturers = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            average_grades_lecturers += lecturer.grades[course_name]

    if len(average_grades_lecturers) == 0:
        return 'Нет оценок'

    return sum(average_grades_lecturers) / len(average_grades_lecturers)


student_1 = Student('Ivan', 'Ivanov', 'male')
student_2 = Student('Olesya', 'Zadova', 'female')
student_3 = Student('Arseniy', 'Uglov', 'male')

student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_3.courses_in_progress += ['Python']

mentor_1 = Mentor('Vladimir', 'Pupkin')
mentor_2 = Mentor('Klava', 'Zalupina')

mentor_1.courses_attached += ['Python']
mentor_2.courses_attached += ['Git']

lecturer_1 = Lecturer('Sava', 'Golovkin')
lecturer_2 = Lecturer('Inessa', 'Durova')
lecturer_3 = Lecturer('Pipin', 'Korotkiy')

lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']
lecturer_3.courses_attached += ['Git']

reviewer_1 = Reviewer('Igor', 'Zvyagin')
reviewer_2 = Reviewer('Anna', 'Nosova')

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 3)
student_1.rate_w(lecturer_1, 'Python', 4)

reviewer_2.rate_hw(student_2, 'Git', 1)

# Вызываем метод __str__
print(student_1)

print(lecturer_1)

# Вызываем метод __lt__
print(student_2 < student_1)

student_list = [student_1, student_3]

print(get_average_grade_student(student_list, 'Python'))

lecturer_list = [lecturer_2, lecturer_3]

print(get_average_grade_lecturers(lecturer_list, 'Git'))
