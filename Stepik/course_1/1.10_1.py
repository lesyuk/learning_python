A = int(input())
B = int(input())
H = int(input())

if B >= H >= A:
    print("Это нормально")
elif H < A:
    print("Недосып")
else:
    print("Пересып")