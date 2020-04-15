s = input()
s = s.replace(s[s.find('h'):s.rfind('h') + 1], '', 1)
print(s)