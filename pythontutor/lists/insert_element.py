l = [int(i) for i in input().split()]
k, c = [int(i) for i in input().split()]
l.insert(k, c)
print(*l)