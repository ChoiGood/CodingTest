# RGB 거리


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2]

for i in range(1, N):
    for j in range(3):
        # 이 부분 더 예쁘게 못짜나?
        tmp_min = 0
        if j == 0:
            tmp_min = min(dp[i - 1][1], dp[i - 1][2])
        if j == 1:
            tmp_min = min(dp[i - 1][0], dp[i - 1][2])
        if j == 2:
            tmp_min = min(dp[i - 1][0], dp[i - 1][1])

        dp[i][j] = arr[i][j] + tmp_min

print(min(dp[N - 1]))