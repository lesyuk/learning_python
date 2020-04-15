sum = 0
n = 1
for i in range(1, int(input()) + 1):
    for j in range(1, i + 1):
        n *= j
    sum += n
    n = 1
print(sum)