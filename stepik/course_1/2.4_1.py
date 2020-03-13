gc = input()
c = 0

gc = gc.upper()

for i in gc:
    if i == 'G':
        c += 1
    elif i == 'C':
        c += 1

print(c / len(gc) * 100)