import sys

N, M = map(int, input().split())

lst = list(map(int, input().split())) # 문제 lst 입력
lst.insert(0, 0) # lst index에 숫자 1 3 그대로 접근하기 위해 insert

# 누적합 구하기
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + lst[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(s[j] - s[i - 1])

