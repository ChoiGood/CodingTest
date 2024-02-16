# LCS 2
# Longest Common Subsequence, 최장 공통 부분 수열

# 입력
s1 = input()
s2 = input()

# 문자열의 길이
n = len(s1) # 첫번쨰 문자열의 길이
m = len(s2) # 두번쨰 문자열의 길이

dp = [[''] * (n + 1) for _ in range(m + 1)] # 행 : 두번째 문자열 열 : 첫번째 문자열
# dp 와 Indexing을 편하게 쓰기위해 문자열 전처리
s1 = '0' + s1 
s2 = '0' + s2

# dp 구현
# ACAYKP, CAPCAK 가 주어졌을 때
# dp[i][j] 는 1~i 까지의 문자열과 1~j까지의 문자열의 최장 공통부분을 의미
# 이는 dp의 앞쪽의 정보들로 만들 수 있다
# 규칙
# 서칭하는 문자열이 같을 때 : dp의 왼쪽 대각선 값 + 1 => dp[i - 1][j - 1] + 1
# 서칭하는 문자열이 다를 때 : dp의 왼쪽값과 위쪽값 중 최댓값 => max(dp[i - 1][j], dp[i][j - 1]) 

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s2[i] == s1[j]:
            dp[i][j] = dp[i - 1][j - 1] + s2[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[m][n]))
print(dp[m][n])