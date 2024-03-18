# 빙산
from collections import deque
import sys
sys.setrecursionlimit(10000)

d_r = [-1, 1, 0, 0]
d_c = [0, 0 , -1, 1]

def bfs(row, col, visited, isice):
    visited[row][col] = True #방문 처리
    dq = deque()
    dq.append((row, col))

    # bfs 이동 하면서 주변에 빙산이 있으면 상하좌우로 녹이기
    while dq:
        r, c = dq.popleft()

        for d in range(4):
            n_r = r + d_r[d]
            n_c = c + d_c[d]

            if 0 <= n_r < N and 0 <= n_c < M: # 범위 안
                # 상하 좌우로 녹이기
                if arr[n_r][n_c] == 0 and not isice[n_r][n_c]:
                    if arr[r][c] > 0:
                        arr[r][c] -= 1

                if not visited[n_r][n_c] and isice[n_r][n_c]:
                    visited[n_r][n_c] = True
                    dq.append((n_r, n_c))

def melt():
    visited = [[True] * M for _ in range(N)]
    isice = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                visited[i][j] = False
                isice[i][j] = True

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                bfs(i, j, visited, isice)

def dfs(row, col, visited):
    visited[row][col] = True
    for d in range(4):
        n_r = row + d_r[d]
        n_c = col + d_c[d]

        if 0 <= n_r < N and 0 <= n_c < M and not visited[n_r][n_c] and arr[n_r][n_c] > 0:
            dfs(n_r, n_c, visited)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

t = 0
is_result = False

while True:
    # 0. 시간 더하기
    t += 1
    # 1. 빙산 녹이기
    melt()

    # 빙산 덩어리 test
    # 2개 이상 -> 나가고 t 출력
    # 0이면 0 출력
    cnt = 0 # 빙산 덩어리 개수
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] > 0:
                dfs(i, j, visited)
                cnt += 1

    if cnt == 0:
        break

    if cnt >= 2:
        is_result = True
        break

print(t if is_result else 0)