s = input()
ns = ''
for i in range(len(s)):
    if i % 3 != 0:
        ns += s[i]
print(ns)