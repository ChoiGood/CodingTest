# 골드바흐 파티션
# 골드바흐의 추측 : 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
import math
# 소수 체크 : 아리스토테네스의 체 만들어서 구현
prime_list = [0] * 1000001

for i in range(2, 1000001):
    prime_list[i] = i

for i in range(2, int(math.sqrt(1000001)) + 1):
    if prime_list[i] != 0:
        for j in range(2 * i, 1000001, i):
            prime_list[j] = 0


# 만든 소수로 소수들의 합으로 표현 되는걸 어떻게 만들지??
T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(N//2 + 1):
        if prime_list[i] != 0 and prime_list[N - i] != 0:
            cnt += 1
    print(cnt)
        
    