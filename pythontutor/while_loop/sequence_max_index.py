x = 0
i = 0
c = -1
n = int(input())
while n != 0:
    c += 1
    if n > x:
        x = n
        i = c
    n = int(input())
print(i)