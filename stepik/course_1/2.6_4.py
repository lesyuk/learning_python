m = []
s = ''

while s != 'end':
    s = input()
    if s != 'end':
        m += [[int(i) for i in s.split()]]
    else:
        continue

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i - 1][j] + m[i - len(m) + 1][j] + m[i][j - 1] + m[i][j - len(m[i]) + 1], end=' ')
    print()