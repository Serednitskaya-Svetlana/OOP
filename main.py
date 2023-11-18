def average_courses_stud(students_list, course):
    for student in students_list:
        for cours_name, average in student.grades_stud.items():
            if course == cours_name:
                average_sum = sum(average) / len(average)
                print(f'Студент: {student.name} {student.surname}\n'
                    f'Курс: {cours_name}\n'
                    f'Средняя оценка за лекции: {round(average_sum, 1)}')

def average_courses_lec(lecturers_list, course):
    for lecturer in lecturers_list:
        for cours_name, average in lecturer.grades_lec.items():
            if course == cours_name:
                average_sum = sum(average) / len(average)
                print(f'Лектор: {lecturer.name} {lecturer.surname}\n'
                    f'Курс: {cours_name}\n'
                    f'Средняя оценка за лекции: {round(average_sum, 1)}')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_stud = {}

    def rate_hw_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade]
            else:
                lecturer.grades_lec[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades_stud(self):
        grades_stud_count = 0
        grades_stud_sum = 0
        for grade in self.grades_stud:
            grades_stud_count += len(self.grades_stud[grade])
            grades_stud_sum += sum(self.grades_stud[grade])
        if (grades_stud_sum / grades_stud_count) == 0:
            return f'Оценок нет'
        else:
            return grades_stud_sum / grades_stud_count

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции:{self.average_grades_stud()}\n"
                f"Курсы в процессе изучения: "
                f"{','.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {','.join(self.finished_courses)}")

    def __it__(self, other):
        if isinstance(other, Student):
            return self.average_grades_stud() < other.average_grades_stud()
        else:
            return "Ошибка"

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grades_stud() <= other.average_grades_stud()
        else:
            return "Ошибка"

    def __eg__(self, other):
        if isinstance(other, Student):
            return self.average_grades_stud() == other.average_grades_stud()
        else:
            return "Ошибка"

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grades_stud() != other.average_grades_stud()
        else:
            return "Ошибка"

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grades_stud() > other.average_grades_stud()
        else:
            return "Ошибка"

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grades_stud() >= other.average_grades_stud()
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lec = {}

    def average_grades_lec(self):
        grades_lec_count = 0
        grades_lec_sum = 0
        for grade in self.grades_lec:
            grades_lec_count += len(self.grades_lec[grade])
            grades_lec_sum += sum(self.grades_lec[grade])
        if (grades_lec_sum / grades_lec_count) == 0:
            return f'Оценок нет'
        else:
            return grades_lec_sum / grades_lec_count

    def median(self):
        res = {key : float(sum(values)) / len(values)
               for key, values in self.grades_lec.items()}
        if len(self.grades_lec) == 0:
            return 'Оценок нет'
        else:
            return res

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции:{self.average_grades_lec()}")

    def __it__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lec() < other.average_grades_lec()
        else:
            return "Ошибка"

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lec() <= other.average_grades_lec()
        else:
            return "Ошибка"

    def __eg__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lec() == other.average_grades_lec()
        else:
            return "Ошибка"

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lec() != other.average_grades_lec()
        else:
            return "Ошибка"

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lec() > other.average_grades_lec()
        else:
            return "Ошибка"

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lec() >= other.average_grades_lec()
        else:
            return "Ошибка"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades_stud:
                student.grades_stud[course] += [grade]
            else:
                student.grades_stud[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Alisa', 'Selezneva', 'woman')
student_1.finished_courses += ['Git', 'Java']
student_1.courses_in_progress += ['Python']
student_1.grades = {}
student_2 = Student('Kolya', 'Gerasimov', 'man')
student_2.finished_courses += ['Python']
student_2.courses_in_progress += ['Git', 'Java']
student_2.grades = {}
student_3 = Student('Fima', 'Korolev', 'man')
student_3.finished_courses += ['Git']
student_3.courses_in_progress += ['Python']
student_3.grades = {}
student_4 = Student('Ylya', 'Gribkova', 'woman')
student_4.finished_courses += ['Git', 'Java']
student_4.courses_in_progress += ['Python']
student_4.grades = {}
student_5 = Student('Kolya', 'Sulim', 'man')
student_5.finished_courses += ['Python']
student_5.courses_in_progress += ['Git', 'Java']
student_5.grades = {}
student_6 = Student('Kolya', 'Sadovskiy', 'man')
student_6.finished_courses += ['Git']
student_6.courses_in_progress += ['Python']
student_6.grades = {}
student_7 = Student('Mila', 'Rutkevich', 'woman')
student_7.finished_courses += ['Java']
student_7.courses_in_progress += ['Python']
student_7.grades = {}
student_8 = Student('Borya', 'Messerer', 'man')
student_8.finished_courses += ['Python', 'Java']
student_8.courses_in_progress += ['Git']
student_8.grades = {}
student_9 = Student('Ekaterina', 'Mihaylova', 'woman')
student_9.finished_courses += ['Git']
student_9.courses_in_progress += ['Python']
student_9.grades = {}
student_10 = Student('Albina', 'Fetisova', 'woman')
student_10.finished_courses += ['Git']
student_10.courses_in_progress += ['Python', 'Java']
student_10.grades = {}

lecturer_1 = Lecturer('Mihaylo', 'Lomonosov')
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_1.grades = {}
lecturer_2 = Lecturer('Dmitriy', 'Mendeleev')
lecturer_2.courses_attached += ['Python']
lecturer_2.grades = {}
lecturer_3 = Lecturer('Konstantin', 'Tsiolkovskiy')
lecturer_3.courses_attached += ['Git']
lecturer_3.grades = {}
lecturer_4 = Lecturer('Igor', 'Kurchatov')
lecturer_4.courses_attached += ['Java']
lecturer_4.grades = {}

reviewer_1 = Reviewer('Ivan', 'Pavlov')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2 = Reviewer('Aleksandr', 'Popov')
reviewer_2.courses_attached += ['Python']
reviewer_3 = Reviewer('Nikolay', 'Semashko')
reviewer_3.courses_attached += ['Git']
reviewer_4 = Reviewer('Vasiliy', 'Petrov')
reviewer_4.courses_attached += ['Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_4.rate_hw(student_1, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_3.rate_hw(student_2, 'Git', 8)
reviewer_4.rate_hw(student_2, 'Java', 10)
reviewer_1.rate_hw(student_3, 'Python', 9)
reviewer_3.rate_hw(student_3, 'Git', 9)
reviewer_2.rate_hw(student_4, 'Python', 10)
reviewer_1.rate_hw(student_4, 'Git', 10)
reviewer_4.rate_hw(student_4, 'Java', 9)
reviewer_1.rate_hw(student_5, 'Python', 8)
reviewer_3.rate_hw(student_5, 'Git', 10)
reviewer_4.rate_hw(student_5, 'Java', 9)
reviewer_2.rate_hw(student_6, 'Python', 10)
reviewer_1.rate_hw(student_6, 'Git', 10)
reviewer_1.rate_hw(student_7, 'Python', 7)
reviewer_4.rate_hw(student_7, 'Java', 8)
reviewer_2.rate_hw(student_8, 'Python', 10)
reviewer_3.rate_hw(student_8, 'Git', 10)
reviewer_4.rate_hw(student_8, 'Java', 10)
reviewer_1.rate_hw(student_9, 'Python', 9)
reviewer_1.rate_hw(student_9, 'Git', 8)
reviewer_2.rate_hw(student_10, 'Python', 10)
reviewer_3.rate_hw(student_10, 'Git', 9)
reviewer_4.rate_hw(student_10, 'Java', 10)

student_1.rate_hw_lecturer(lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(lecturer_2, 'Python', 9)
student_2.rate_hw_lecturer(lecturer_3, 'Git', 9)
student_2.rate_hw_lecturer(lecturer_4, 'Java', 10)
student_3.rate_hw_lecturer(lecturer_1, 'Python', 7)
student_3.rate_hw_lecturer(lecturer_2, 'Python', 10)
student_4.rate_hw_lecturer(lecturer_3, 'Git', 9)
student_4.rate_hw_lecturer(lecturer_4, 'Java', 10)
student_5.rate_hw_lecturer(lecturer_1, 'Python', 8)
student_5.rate_hw_lecturer(lecturer_2, 'Python', 9)
student_6.rate_hw_lecturer(lecturer_3, 'Git', 10)
student_6.rate_hw_lecturer(lecturer_1, 'Python', 7)
student_7.rate_hw_lecturer(lecturer_4, 'Java', 9)
student_8.rate_hw_lecturer(lecturer_1, 'Python', 10)
student_9.rate_hw_lecturer(lecturer_1, 'Git', 10)
student_10.rate_hw_lecturer(lecturer_1, 'Git', 8)

students_list = [student_1, student_2, student_3, student_4, student_5,
                 student_6, student_7, student_8, student_9, student_10]
lecturers_list = [lecturer_1, lecturer_2, lecturer_3, lecturer_4]

print(student_1 > student_2)
print()
print(lecturer_1 > lecturer_4)
print()
print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(f"Средняя оценка всех студентов по курсу {'Git'}: {average_courses_stud(students_list, 'Git')}")
print()
print(f"Средняя оценка всех лекторов по курсу {'Java'}: {average_courses_lec(lecturers_list, 'Java')}")
print()
print()
