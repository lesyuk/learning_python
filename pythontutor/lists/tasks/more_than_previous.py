x = [int(i) for i in input().split()]
for i in range(1, len(x)):
    if x[i] > x[i-1]:
        print(x[i])