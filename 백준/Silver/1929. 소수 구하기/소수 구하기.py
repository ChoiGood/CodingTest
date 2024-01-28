# 아리스토테네스의 체
import math

M, N = map(int, input().split())

prime_list = [0] * 1000001
for i in range(2, 1000001):
    prime_list[i] = i

for i in range(2, int(math.sqrt(1000001)) + 1):
    if prime_list[i] == 0 :
        continue
    for j in range(2 * i, N + 1, i):
        prime_list[j] = 0


for i in range(M, N + 1):
    if prime_list[i] != 0:
        print(prime_list[i])