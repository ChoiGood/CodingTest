# 01 타일
# N 의 범위 : 1 <= N <= 1,000,000
# 1번 방식으로 값을 나열하니까 피보나치 수열인 것을 발견!!!



# Top - down
dp = [0] * 1000001
def fibo(n):
    if n == 0 or n == 1:
        return 1

    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = (fibo(n - 1) + fibo(n - 2)) % 15746

    return dp[n]

N = int(input())
for i in range(N): # 함수 호출 ==> 비용이 드는 구나 ==> 우리는 bottom up 으로 짜야한다
    fibo(i)
print(fibo(N))

# # Process finished with exit code -1073741571 (0xC00000FD)

# Bottom up
# dp2 = [0] * (1000001)
# dp2[0], dp2[1] = 1, 1
# for i in range(2, 1000000 + 1):
#     dp2[i] = (dp2[i - 1] + dp2[i - 2]) % 15746
#
# N = int(input())
# print(dp2[N])


# # 1. 수학적으로 해결 ==> 시간 초과
# import math
# N = int(input())
# zeros = list(range(N // 2 + 1))
#
# cnt = 0
# for x in zeros:
#     cnt += math.comb(N - x, N - 2*x) # ==> 여기서 나는군...
# print(cnt)


