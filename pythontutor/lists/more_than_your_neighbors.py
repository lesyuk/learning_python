x = [int(i) for i in input().split()]
c = 0
for i in range(1, len(x) - 1):
    if x[i] > (x[i - 1] + x[i + 1]):
        c += 1

print(c)