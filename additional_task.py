grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
#print('List:', students_list)
average0 = sum(grades[0]) / len(grades[0])
average1 = sum(grades[1]) / len(grades[1])
average2 = sum(grades[2]) / len(grades[2])
average3 = sum(grades[3]) / len(grades[3])
average4 = sum(grades[4]) / len(grades[4])
#print(average0, average1, average2, average3, average4)
academic_achievement = {students_list[0] : average0, students_list[1] : average1, students_list[2] : average2, students_list[3] : average3, students_list[4] : average4}
print(academic_achievement)