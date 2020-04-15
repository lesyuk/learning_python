s = input()
space = s.find(' ')
ns = s[space + 1:] + s[space] + s[:space]
print(ns)