students_number_1 = int(input())
students_number_2 = int(input())
students_number_3 = int(input())

desks_number_1 = (students_number_1 // 2) + (students_number_1 % 2)
desks_number_2 = (students_number_2 // 2) + (students_number_2 % 2)
desks_number_3 = (students_number_3 // 2) + (students_number_3 % 2)

print(desks_number_1 + desks_number_2 + desks_number_3)
