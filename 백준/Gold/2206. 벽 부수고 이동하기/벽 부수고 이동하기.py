# 벽 부수고 이동하기
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from collections import deque

INF = 999999999999999
d_r = [-1, 1, 0, 0]
d_c = [0, 0, -1, 1]

mn_distance = INF

def bfs(row, col):
    if N == 1 and M == 1:
        return 1
    visited1 = [[False] * M for _ in range(N)] # 벽을 부술수 있을 때
    visited2 = [[False] * M for _ in range(N)] # 벽을 부술수 없을 때
    dq = deque()
    dq.append((row, col, 1, True))
    visited1[row][col] = True # 방문 처리
    while dq:
        r, c, dist, c_flag = dq.popleft()

        for d in range(4):
            n_r = r + d_r[d]
            n_c = c + d_c[d]

            if 0 <= n_r < N and 0 <= n_c < M: # 범위 안이고

                if c_flag: # 벽을 부술 수 있을 때
                    if arr[n_r][n_c] == 0 and not visited1[n_r][n_c]:
                        visited1[n_r][n_c] = True
                        dq.append((n_r, n_c, dist + 1, c_flag))
                    if arr[n_r][n_c] == 1 and not visited1[n_r][n_c]:
                        visited1[n_r][n_c] = True
                        dq.append((n_r, n_c, dist + 1, False))
                else: # 벽을 부술 수 없을 때
                    if arr[n_r][n_c] == 0 and not visited2[n_r][n_c]:
                        visited2[n_r][n_c] = True
                        dq.append((n_r, n_c, dist + 1, c_flag))


            if n_r == N - 1 and n_c == M - 1:
                return dist + 1

    return -1


N, M = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]

result = bfs(0, 0)
print(result)