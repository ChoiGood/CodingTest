# 스티커
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수

for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # dp 선언 및 초기화
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n > 1:
        dp[0][1] = arr[0][1] + dp[1][0] 
        dp[1][1] = arr[1][1] + dp[0][0]

    # dp[i][j] : 해당 지점에서 가장 큰 가중치
    # 지그재그로 가면서 건너뛰는게 더 클 때는 건너 뛰기
    for i in range(2, n):

        dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2])
    
    print(max(dp[0][n-1], dp[1][n-1]))
    