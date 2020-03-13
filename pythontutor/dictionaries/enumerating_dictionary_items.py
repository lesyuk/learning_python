A = dict(zip('abcdef', list(range(6))))
for key in A:
    print(key, A[key])

for key, val in A.items():
    print(key, val)