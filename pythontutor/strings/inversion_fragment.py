s = input()
fragment = s[s.find('h'):s.rfind('h') + 1]
print(s.replace(fragment, fragment[::-1]))