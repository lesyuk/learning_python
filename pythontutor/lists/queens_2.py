h = [0] * 8
v = [0] * 8
flag = False

for i in range(8):
    h[i], v[i] = [int(i) for i in input().split()]

for i in range(8):
    for j in range(i + 1, 8):
        if (h[i] == h[j] or v[i] == v[j]) or abs(h[i] - h[j]) == abs(v[i] - v[j]):
            flag = True

if flag:
    print('YES')
else:
    print('NO')