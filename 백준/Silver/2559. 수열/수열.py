# 입력
N, K = map(int, input().split())
temp_lst = list(map(int, input().split()))

# 처리 (로직)
# 누적합 구하기
temp_lst.insert(0, 0)
S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i - 1] + temp_lst[i]

# 연속되는 k일의 온도의 합이 최대가 되는 값 구하기
max_temp = S[K] - S[0]
for i in range(K, N + 1):     # i : K -> N
    temp = S[i] - S[i - K]
    if max_temp < temp:
        max_temp = temp
# 출력
print(max_temp)
    