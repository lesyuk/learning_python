N, K = [int(i) for i in input().split()]
bowling_pins = []
for i in range(N):
    bowling_pins.append('I')
for i in range(K):
    f, l = [int(i) for i in input().split()]
    for j in range(f - 1, l):
        bowling_pins[j] = '.'
print(*bowling_pins, sep ='')