a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b or a == b:
    range_1 = a - b
    min_1 = b
else:
    range_1 = b - a
    min_1 = a
if c > d or c == d:
    range_2 = c - d
    min_2 = d
else:
    range_2 = d - c
    min_2 = c

print(' ', '\t', end='')
for i in range(range_2 + 1):
    print(min_2 + i, '\t', end='')
print()
for h in range(range_1 + 1):
    print(min_1 + h, '\t', end='')
    for j in range(range_2 + 1):
        print((min_2+j) * (min_1+h), '\t', end='')
    print()