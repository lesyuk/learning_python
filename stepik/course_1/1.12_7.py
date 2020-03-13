ticket_id = int(input())

digit_1 = ticket_id // 100000
digit_2 = ticket_id // 10000 % 10
digit_3 = ticket_id // 1000 % 10
digit_4 = ticket_id % 1000 // 100
digit_5 = ticket_id % 100 // 10
digit_6 = ticket_id % 10

if digit_1 + digit_2 + digit_3 == digit_4 + digit_5 + digit_6:
    print("Счастливый")
else:
    print("Обычный")