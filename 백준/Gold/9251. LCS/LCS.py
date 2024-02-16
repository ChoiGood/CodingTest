# LCS
# 최장 공통 부분 수열

s1 = list(input())
s2 = list(input())

# n : 첫 번째 문자열의 길이, m : 두 번째 문자열의 길이
n, m = len(s1), len(s2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

# 인덕스를 동일하게 접근하기 위해 (dp, s1, s2)
s1.insert(0, 0)
s2.insert(0, 0)

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[j] != s2[i]: # 문자가 다르면 왼쪽과 위쪽 값들 중 더 큰 값을 대입
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else: # 문자가 같다면 왼쪽 대각선 위의 값에서 +1 해주기
            dp[i][j] = dp[i - 1][j - 1] + 1

print(dp[m][n])



