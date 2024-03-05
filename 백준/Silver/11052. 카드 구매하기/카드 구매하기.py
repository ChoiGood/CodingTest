# 카드 구매하기
N = int(input()) # 구매하려고 하는 카드의 개수
P = list(map(int, input().split())) # 카드팩의 가격
M = len(P) # 카드팩의 개수
P.insert(0, 0)

# 일단 이차원 dp로 구현해보기.
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(i):
        dp[i][j] = dp[i - 1][j]
    
    for j in range(i, N + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - i] + P[i])

print(dp[M][N])