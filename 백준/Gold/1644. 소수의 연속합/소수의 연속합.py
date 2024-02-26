# 소수의 연속합
Prime_Length = 4000001

prime = [0] * Prime_Length

for i in range(2, Prime_Length):
    prime[i] = i

for i in range(2, Prime_Length):
    if prime[i] == 0:
        continue
    for j in range(i*i, Prime_Length, i):
        prime[j] = 0

N = int(input())
# N 이하의 소수 가져오기
S = [0] # 누적합
for i in range(2, N + 1):
    if prime[i] != 0:
        S.append(i)

for i in range(1, len(S)):
    S[i] += S[i - 1]

# 투 포인터 알고리즘
cnt = 0 # 소수의 합으로 표현 가능한 경우의 수
i, j = 0, 1
while i < len(S) and j < len(S):
    value = S[j] - S[i]
    if value < N:
        j += 1
    elif value == N:
        cnt += 1
        j += 1
    else:
        i += 1

print(cnt)