n = int(input())
_ = 2
if n == 0:
    print(0)
else:
    a, b = 0, 1
    while _ <= n:
        a, b = b, a + b
        _ += 1
print(b)
