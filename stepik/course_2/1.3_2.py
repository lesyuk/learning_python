n, k = map(int, input().split())
cnk = 0


def func(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return func(n - 1, k) + func(n - 1, k - 1)

print(func(n, k))