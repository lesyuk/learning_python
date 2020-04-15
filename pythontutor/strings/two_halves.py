s = input()
print(s[len(s) // 2 + len(s) % 2:] + s[:len(s) // 2 + len(s) % 2])