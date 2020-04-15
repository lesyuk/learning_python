l, k = input().split(), int(input())
for i in range(k + 1, len(l)):
    l[k] = l[i]
    k += 1
l.pop()
print(*l)