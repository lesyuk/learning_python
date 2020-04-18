N = int(input())
n_sum = 0
input_sum = 0
for i in range(1, N + 1):
    n_sum += i
for i in range(N - 1):
    input_sum += int(input())
print(n_sum - input_sum)
