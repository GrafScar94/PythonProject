grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Для начала перведем множество students в список и отсортируем его по алфавиту.
students = list(students)
sort_ = students.sort()
print(students)
# Затем вычислим средний балл в каждом из списков оценок списка grades.
grades[0] = sum(grades[0]) / len(grades[0])
grades[1] = sum(grades[1]) / len(grades[1])
grades[2] = sum(grades[2]) / len(grades[2])
grades[3] = sum(grades[3]) / len(grades[3])
grades[4] = sum(grades[4]) / len(grades[4])
print(grades)
# Таким образом у нас получилось два списка, которые нам необходимо объединить в словарь.
# Так как список grades изначально был упорядочен согласно алфавитному порядку учеников, то нам остается просто объединить их.
average_student_score = dict(zip(students, grades))
print(average_student_score)


