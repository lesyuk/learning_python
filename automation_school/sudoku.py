l = [[int(i) for i in input().split()] for j in range(3)]
allowable_range = [i for i in range(1, 10)]
s = set()
valid_field = True

for i in l:
    for j in i:
        s.add(j)

for i in allowable_range:
    if i in s:
        valid_field = True
    else:
        valid_field = False

if valid_field:
    print('Все хорошо')
else:
    print(':(')