l = input().split()
flag = True
unique_list = []
for i in range(len(l)):
    for j in range(i - 1, -(len(l) - i), -1):
        if l[i] == l[j]:
            flag = False
    if flag:
        unique_list.append(l[i])
    flag = True
print(*unique_list)