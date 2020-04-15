x = int(input())
y = int(input())
d = 1
while y > x:
    d += 1
    x += x * 10 / 100 # находим 10% от x
print(d)
