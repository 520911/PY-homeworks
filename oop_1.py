class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # Словарь с оценками студентов
        self.e_grade = None  # Средняя оценка за домашние задания

    def lectors_grade(self, lector, course, grade):
        """
        Метод суммирует все оценки студентов, проставленных лектору за курс
        :param lector: Экземпляр класса Лектор
        :param course: Название курса
        :param grade: Оценка работы лектора на курсе
        """
        if (isinstance(lector, Lecturer) and course in lector.courses_attached) and \
                (course in self.finished_courses or course in self.courses_in_progress):
            if course in lector.lectors_grades:
                lector.lectors_grades[course] += [grade]
            else:
                lector.lectors_grades[course] = [grade]
        else:
            return print(f'{lector.name + " " + lector.surname} не принадлежит классу Lecturer или '
                         f'{lector.name + " " + lector.surname} не ведет курс {course}!')

    def ever_grade(self):  # Функция вычисления среднего значения оценок студента
        """
        Метод принимает на вход экземпляр класса Student
        При вычислении среднего значения учитывается, что значения словаря с оценками студента будет сложенный список
        :return: Функция возвращает среднюю оценку студента за все курсы
        """
        self.e_grade = \
            (sum(list(map(sum, list(self.grades.values())))) / (sum(list(map(len, list(self.grades.values()))))))
        return self.e_grade

    # def __repr__(self): Пробный метод РЕПР
    #     return f'Имя: {self.name}\n' \
    #            f'Фамилия: {self.surname}\n' \
    #            f'Средняя оценка за домашние задания: ' \
    #            f'{sum(list(self.grades.values())) / len((list(self.grades.values())))}\n' \
    #            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
    #            f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.ever_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):  # < >
        if not isinstance(other, Student):
            print('Не студент!')
        else:
            return self.ever_grade() < other.ever_grade()

    def __eq__(self, other):  # == !=
        if not isinstance(other, Student):
            print('Не студент!')
        else:
            return self.ever_grade() == other.ever_grade()

    def __le__(self, other):  # >= <=
        if not isinstance(other, Student):
            print('Не студент!')
        else:
            return self.ever_grade() <= other.ever_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectors_grades = {}
        self.e_grade = None

    def ever_grade(self):
        """
        Метод принимает на вход экземпляр класса Mentor
        При вычислении среднего значения учитывается, что значения словаря с оценками лектора - вложенный список
        :return: Функция возвращает среднюю оценку лектора за все курсы
        """
        self.e_grade = \
            (sum(list(map(sum, list(self.lectors_grades.values())))) / (
                sum(list(map(len, list(self.lectors_grades.values()))))))
        return self.e_grade

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.ever_grade()}'

    def __lt__(self, other):  # < >
        if not isinstance(other, Lecturer):
            print('Не лектор!')
        else:
            return self.ever_grade() < other.ever_grade()

    def __eq__(self, other):  # == !=
        if not isinstance(other, Lecturer):
            print('Не лектор!')
        else:
            return self.ever_grade() == other.ever_grade()

    def __le__(self, other):  # <= >=
        if not isinstance(other, Lecturer):
            print('Не лектор!')
        else:
            return self.ever_grade() <= other.ever_grade()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def set_grades(self, student, course, grade):
        """
        Метод суммирует все оценки проверяющих в словаре оценок студента
        :param student: Экземпляр класса Student
        :param course: Название курса
        :param grade: Оценка за экзамен
        :return: Обработка ошибки
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'
