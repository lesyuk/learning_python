import datetime

y, m, d = map(int, input().split())
days = int(input())
date = datetime.date(y, m, d)
date += datetime.timedelta(days)
print(date.year, date.month, date.day)