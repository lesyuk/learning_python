max = 0
second_max = 0
n = int(input())
while n != 0:
    if n > max:
        max = n
    if max > second_max < n:
        second_max = n
    n = int(input())
print(second_max)