# 다음 소수
# 이거 시간복잡도 따지기 어렵네.. 
import math
def prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

def next_prime(n):
    while True:
        if(prime(n)):
            break
        else:
            n += 1
    return n


T = int(input())

for _ in range(T):
    number = int(input())
    print(next_prime(number))
