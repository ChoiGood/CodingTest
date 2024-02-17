# 나이트의 이동
from collections import deque
# 델타리스트 (나이트 이동)
d_row = [-2, -2, -1, -1, 1, 1, 2, 2]
d_col = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(row, col):
    chess[row][col] = 0
    dq = deque()
    dq.append((row, col))

    while dq:
        r, c = dq.popleft()
        for d in range(8):
            n_r = r + d_row[d]
            n_c = c + d_col[d]
            if 0 <= n_r < N and 0 <= n_c < N and chess[n_r][n_c] == -1:
                chess[n_r][n_c] = chess[r][c] + 1 # 방문처리
                dq.append((n_r, n_c))
            if n_r == e_r and n_c == e_c:
                return




T = int(input())

for _ in range(T):
    N = int(input())
    s_r, s_c = map(int, input().split())
    e_r, e_c = map(int, input().split())

    chess = [[-1] * N for _ in range(N)]
    bfs(s_r, s_c)

    print(chess[e_r][e_c])
