a = int(input())
b = int(input())
c = int(input())

if a <= b <= c:
    print(a)
elif a <= c <= b:
    print(a)
elif b <= a <= c:
    print(b)
elif b <= c <= a:
    print(b)
elif c <= a <= b:
    print(c)
elif c <= b <= a:
    print(c)
