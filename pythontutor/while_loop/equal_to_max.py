i = 0
l = []
n = int(input())
while n != 0:
    if n > i:
        i = n
    l += [n]
    n = int(input())

print(l.count(i))