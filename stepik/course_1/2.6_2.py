s = int(input())
m = []
c = 0

for i in range(s+1):
    if s > c:
        for j in range(i):
            if s > c:
                m.append(i)
                c += 1
            else:
                break
    else:
        break

print(*m)