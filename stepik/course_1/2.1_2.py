a, b= int(input()), int(input())
if a > b:
    x = a
    while x % a != 0 or x % b != 0:
        x += a
else:
    x = b
    while x % a != 0 or x % b != 0:
        x += b
print(x)