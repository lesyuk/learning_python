a = int(input())
b = int(input())
c = int(input())

if a != b and a != c and b != a and b != c:
    if b > a < c:
        print(a)
    elif a > b < c:
        print(b)
    elif a > c < b:
        print(c)
else:
    if a == b:
        