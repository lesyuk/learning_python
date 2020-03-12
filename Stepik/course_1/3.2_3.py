n = int(input())
d = {}
result = 0
l = []

for i in range(n):
    l += [int(input())]

for key in l:
    if key in d:
        print(d[key])
    else:
        result = f(key) # функция f уже где-то объявлена
        print(result)
        d = {key: result}