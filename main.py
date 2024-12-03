class Information:
    def __str__(self):
        string_for_print = f"Имя: {self.name}\nФамилия: {self.surname}"
        if self.CLASS_TYPE == "lecturer":
            string_for_print += f"\nСредняя оценка за лекции: {self.get_average_rating()}"
        if self.CLASS_TYPE == "student":
            string_for_print += f"\nСредняя оценка за домашние задания: {self.get_average_rating()}"
            string_for_print += f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"
            string_for_print += f"\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return string_for_print

    def get_average_rating(self):
        if self.grades.values():
            grades_lst = [i for a in self.grades.values() for i in a]
            return round(sum(grades_lst) / len(grades_lst), 1)
        return "Оценок нет"


class Student(Information):
    CLASS_TYPE = "student"

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def set_rates(self, lecturer, course, grade):
        if not course in self.courses_in_progress + self.finished_courses:
            raise ValueError("Студент не был на данном курсе")
        if course not in lecturer.courses_attached:
            raise ValueError("Данный лектор не ведёт этот курс")
        if type(grade) != int or grade not in range(1, 11):
            raise TypeError("Оценка должны быть целым числом от 1 до 10")
        lecturer.update_rating()
        lecturer.grades[course] += [grade]


class Mentor(Information):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    CLASS_TYPE = "lecturer"

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def update_rating(self):
        for course in self.courses_attached:
            if course not in self.grades:
                self.grades[course] = []


class Reviewer(Mentor):
    CLASS_TYPE = "reviewer"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise ValueError("Ошибка в оценке")




