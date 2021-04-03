from oop_1 import *

# Создание по два экземпляра каждого класса

stu: Student = Student('Student1', 'Student_1', 'male')
stu_2 = Student('Stundet2', 'Stident_2', 'female')
men = Mentor('Mentor1', 'Mentor_1')
men_2 = Mentor('Mentor2', 'Mentor_2')
lec = Lecturer('Lector1', 'Lector_1')
lec_2 = Lecturer('Lector2', 'Lector_2')
rev = Reviewer('Reviewer1', 'Reviewer_1')
rev_2 = Reviewer('Reviewer2', 'Reviewer_2')

# "Наполнение" студентов курсами

stu.courses_in_progress += ['python', 'java']
stu_2.courses_in_progress += ['node.js', 'js']
stu.finished_courses += ['node.js', 'js']
stu_2.finished_courses += ['python', 'django']
print(f'Курсы, которые окончил первый студент: {stu.finished_courses}\n'
      f'Курсы, которые окончил второй студент:{stu_2.finished_courses}\n'
      f'Курсы, на которых учится первый студент: {stu.courses_in_progress}\n'
      f'Курсы, на которых учится второй студент: {stu_2.courses_in_progress}')
print()

# "Наполнение" проверяющих и лекторов курсами

lec.courses_attached += ['python', 'java']
lec_2.courses_attached += ['node.js', 'js']
rev.courses_attached += ['python', 'java']
rev_2.courses_attached += ['node.js', 'js']
print(f'Курсы, которые проверяет первый Reviewer: {rev.courses_attached}\n'
      f'Курсы, которые проверяет вротой Reviewer: {rev_2.courses_attached}\n'
      f'Курсы, которые ведет первый лектор: {lec.courses_attached}\n'
      f'Курсы, которые ведет второй лектор: {lec_2.courses_attached}')

# Reviewer проставляют оценки студентам

rev.set_grades(stu, 'python', 10)
rev.set_grades(stu, 'java', 9)
rev.set_grades(stu, 'java', 5)
rev_2.set_grades(stu_2, 'node.js', 8)
rev_2.set_grades(stu_2, 'js', 7)
rev_2.set_grades(stu_2, 'js', 8)
print()

# Проверка оценок за курсы у студентов

print(f'Оценки за курсы первого студента: {stu.grades}')
print(f'Оценки за курсы второго студента: {stu_2.grades}')

# Проставляет оценки лекторам за курсы

stu.lectors_grade(lec, 'python', 8)
stu.lectors_grade(lec, 'java', 10)
stu_2.lectors_grade(lec, 'python', 9)
stu.lectors_grade(lec, 'java', 8)
stu.lectors_grade(lec_2, 'node.js', 7)
stu_2.lectors_grade(lec_2, 'node.js', 10)
stu.lectors_grade(lec_2, 'js', 9)
stu_2.lectors_grade(lec_2, 'js', 7)
print(f'Оценки студентов за курсы первого лектора: {lec.lectors_grades}')
print(f'Оценки студентов за курсы второго лектора: {lec_2.lectors_grades}')
print()

# Вывод информации о студентах, лекторах и проверяющих

print(stu, stu_2, lec, lec_2, rev, rev_2, sep='\n\n')
print()

# Сравнение лекторов и студентов по средним оценкам

print(stu == stu_2)
print(stu != stu_2)
print(stu < stu_2)
print(stu > stu_2)
print(stu <= stu_2)
print(stu >= stu_2)
print(lec == lec_2)
print(lec != lec_2)
print(lec >= lec_2)
print(lec <= lec_2)
print(lec > lec_2)
print(lec < lec_2)

print()

studentss_list = [stu, stu_2]
lectorss_list = [lec, lec_2]


def grades_everage_of_students_courses(students_list, course_name):
    for student in students_list:
        for courses in list(student.grades.keys()):
            if courses == course_name:
                print(courses, student.name, sum(student.grades[courses]) / len(student.grades[courses]))


def grades_everage_of_lectors_courses(lectors_list, course_name):
    for lector in lectors_list:
        for courses in list(lector.lectors_grades.keys()):
            if courses == course_name:
                print(courses, lector.name, sum(lector.lectors_grades[courses]) / len(lector.lectors_grades[courses]))


grades_everage_of_students_courses(studentss_list, 'python')
grades_everage_of_students_courses(studentss_list, 'js')
grades_everage_of_students_courses(studentss_list, 'java')
grades_everage_of_students_courses(studentss_list, 'node.js')
print()
grades_everage_of_lectors_courses(lectorss_list, 'python')
grades_everage_of_lectors_courses(lectorss_list, 'java')
grades_everage_of_lectors_courses(lectorss_list, 'node.js')
grades_everage_of_lectors_courses(lectorss_list, 'js')
