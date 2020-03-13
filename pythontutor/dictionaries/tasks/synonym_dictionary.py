c = int(input())
d = {}
for i in range(c):
    k, v = input().split()
    d[k] = v
word = input()

[print(d) for d, v in d.items() if v == word]
