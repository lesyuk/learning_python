c = -1
previous_n = 0
n = int(input())
while n != 0:
    if n > previous_n:
        c += 1
    previous_n = n
    n = int(input())
print(c)