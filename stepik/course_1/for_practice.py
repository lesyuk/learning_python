for i in range(9):
    for k in range(9-i):
        print(' ', end=' ')
    for j in range(i+1):
        print(j+1, end=' ')
    for h in range(j):
        print(j-h, end=' ')
    print()
for i in range(8):
    for j in range(i+2):
        print(' ', end=' ')
    for j in range(8-i):
        print(j+1, end=' ')
    for h in range(j):
        print(j-h, end=' ')
    print()
