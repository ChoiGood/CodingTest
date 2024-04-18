# # 행렬 곱셈 순서
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# matrix_info = [tuple(map(int, input().split())) for _ in range(n)]
#
# # dp 선언
# dp = [[float('inf')] * n for _ in range(n)]
# 
# # dp 초기화
# for i in range(n):
#     dp[i][i] = 0
#
# for i in range(1, n):
#     for j in range(n - i):
#         for k in range(j, j + i):
#             prod = matrix_info[j][0] * matrix_info[k][1] * matrix_info[j+i][1]
#             dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + prod)
#
# # for a in dp:
# #     print(*a)
# print(dp[0][n-1])

# ================================================
# 변수의 지역성을 고려한 코드로 업그레이드
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
m = [[0]*(N+1) for _ in range(N+1)]

p = []
a,b = map(int,input().split())
p.append(a)
p.append(b)
for i in range(1, N):
    a,b = map(int,input().split())
    p.append(b)

for i in range(1,N+1):
    m[i][i] = 0 # 초깃값 셋팅 (i=j인 경우들)

for i in range(1, N+1) :
    for j in range(i-1, 0,-1) :
        min_value = INF
        for k in range(j,i) :
            temp_value = m[j][k]+m[k+1][i]+p[j-1]*p[k]*p[i]
            if min_value > temp_value :
                min_value = temp_value
        m[j][i]= min_value

print(m[1][N])