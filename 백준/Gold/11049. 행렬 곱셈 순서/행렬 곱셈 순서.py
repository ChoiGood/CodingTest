# 행렬 곱셈 순서
import sys
input = sys.stdin.readline

n = int(input())
matrix_info = [tuple(map(int, input().split())) for _ in range(n)]

# dp 선언
dp = [[float('inf')] * n for _ in range(n)]

# dp 초기화
for i in range(n):
    dp[i][i] = 0

for i in range(1, n):
    for j in range(n - i):
        for k in range(j, j + i):
            prod = matrix_info[j][0] * matrix_info[k][1] * matrix_info[j+i][1]
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + prod)

# for a in dp:
#     print(*a)
print(dp[0][n-1])


