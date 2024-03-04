# 골드바흐의 추측
import sys
input = sys.stdin.readline

eratosthenes = [0] * 1000001
for i in range(2, 1000001):
    eratosthenes[i] = i

for i in range(2, 1000001):
    if eratosthenes[i] == 0: continue
    for j in range(i*i, 1000001, i):
        eratosthenes[j] = 0

while True:
    value = int(input().rstrip())
    if value == 0:
        break

    for odd in range(3, value, 2):
        if eratosthenes[odd] and eratosthenes[value - odd]:
            print(f'{value} = {odd} + {value - odd}')
            break

