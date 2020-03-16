n = int(input())
hours = n // 60
minutes = n % 60
if hours < 24:
    print(hours, minutes)
else:
    print(hours % 24, minutes)