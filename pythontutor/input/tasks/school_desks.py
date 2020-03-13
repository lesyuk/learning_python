student_number_1 = int(input())
student_number_2 = int(input())
student_number_3 = int(input())

number_of_desks_1 = (student_number_1 // 2) + (student_number_1 % 2)
number_of_desks_2 = (student_number_2 // 2) + (student_number_2 % 2)
number_of_desks_3 = (student_number_3 // 2) + (student_number_3 % 2)

print(number_of_desks_1 + number_of_desks_2 + number_of_desks_3)