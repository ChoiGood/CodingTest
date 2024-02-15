# 전깃줄
n = int(input()) # 전깃줄의 개수
arr = [0] * 501 # 위치의 번호는 500 이하의 자연수!
dp = [0] * 501
for _ in range(n):
    a, b = map(int, input().split())
    arr[a] = b

# print(arr)

for i in range(1, 501):
    if arr[i] != 0:
        dp[i] = 1
        for j in range(1, i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
# print(dp)

print(n - max(dp))


