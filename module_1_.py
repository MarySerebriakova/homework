grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
type(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
stud = list(students)
print(stud)
sorted_stud = sorted(stud)
print(sorted_stud)
dict_grade = {}
for grade in grades:
    sum = 0
    for i in range(len(grade)):
        sum = sum + grade[i]
    average_grade = sum/len(grade)
    print(average_grade)
for i in range(len(sorted_stud)):
    dict_grade.update (sorted_stud[i] , average_grade[i])





