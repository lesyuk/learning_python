c = 0
s = 0
while True:
    a = int(input())
    c += a
    s += a ** a
    if c == 0:
        break

print(s)