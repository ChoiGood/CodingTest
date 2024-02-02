N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.insert(0, 0)

# 구간합 구하기
S = [0] * (N + 1)

for i in range(1, N + 1):
    S[i] = S[i - 1] + numbers[i]
# (a + b) % M = a % M + b % M
cnt_lst = [0] * M
for i in range(1, N + 1):
    S[i] %= M
    cnt_lst[S[i]] += 1

# cnt 구하기
S.pop(0)
cnt = 0
cnt += cnt_lst[0]
for i in range(M):
    tmp = cnt_lst[i]
    cnt += (tmp * (tmp - 1)) // 2

print(cnt)


