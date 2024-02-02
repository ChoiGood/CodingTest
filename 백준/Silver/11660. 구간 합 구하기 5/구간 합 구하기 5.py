# 구간 합 구하기 5
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for a in arr:
    a.insert(0, 0)
arr.insert(0, [0] * (N + 1))

S = [[0] * (N + 1) for _ in range(N + 1)]

# 구간합 구하기!!
for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] = S[i][j - 1] + S[i - 1][j] - S[i - 1][j - 1] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1])


