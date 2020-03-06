counter = int(input())
last_digit = counter % 100
if 10 < last_digit < 15:
    print(counter, 'программистов')
else:
    last_digit = last_digit % 10
    if last_digit == 1:
        print(counter, 'программист')
    elif last_digit == 2 or last_digit == 3 or last_digit == 4:
        print(counter, 'программиста')
    else:
        print(counter, 'программистов')
