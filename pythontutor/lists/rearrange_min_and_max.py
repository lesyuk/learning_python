l = [int(i) for i in input().split()]
min_index = 0
max_index = 0
for i in range(len(l)):
    if l[i] < l[min_index]:
        min_index = i
    elif l[i] > l[max_index]:
        max_index = i

l[min_index], l[max_index] = l[max_index], l[min_index]
print(*l)