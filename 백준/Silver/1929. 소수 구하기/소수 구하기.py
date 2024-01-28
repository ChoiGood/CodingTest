# 아리스토테네스의 체
import math

def prime(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_list = [i for i in range(0, 1000001)]

prime_list[1] = -1
for i in range(2, 1000001):
    if prime_list[i] != -1:
        if not prime(prime_list[i]): # 체 업데이트
            for j in range(i, 1000001, i):
                prime_list[j] = -1

M, N = map(int, input().split())

for i in range(M, N + 1):
    if prime_list[i] != -1:
        print(prime_list[i])


