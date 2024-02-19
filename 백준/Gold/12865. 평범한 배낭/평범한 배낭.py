# 평범한 배낭
import sys
input = sys.stdin.readline

# 물품의 수, 무게
N, K = map(int, input().split())

items = [0]
for _ in range(N):
    W, V = map(int, input().split()) # 무게 W, 가치 V
    items.append((W, V))

dp = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(1, K + 1):
    if i >= items[1][0]:
        dp[i][1] = items[1][1]

for w in range(1, K + 1):
    for i in range(2, N + 1):
        if w < items[i][0]: # 넣는 아이템의 무게가 무게 W를 넘는다
            dp[w][i] = dp[w][i - 1]
        else: # 넣는 아이템의 무게가 무게 W를 넘지 않는다
            dp[w][i] = max(dp[w][i - 1], dp[w-items[i][0]][i - 1] + items[i][1])

print(dp[K][N])