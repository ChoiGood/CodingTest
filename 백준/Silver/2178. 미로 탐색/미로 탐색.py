# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

def bfs(row, col):
    dq = deque()
    maze[row][col] = 1 # <- 방문처리 : 이동횟수를 표현!! 출발 지점과 도착 지점도 이동에 포함
    dq.append((row, col))

    while dq:
        r, c = dq.popleft()
        for d in range(4):
            n_r = r + d_row[d]
            n_c = c + d_col[d]
            if 0 <= n_r < N and 0 <= n_c < M: # 미로 안이고
                if maze[n_r][n_c] == 1 and not (n_r == 0 and n_c == 0): # 이동 가능한 통로이며 시작 지점이 아닐 때(시작 지점 값이 1임)
                    maze[n_r][n_c] = maze[r][c] + 1 # 방문처리 (pop한 노드의 값 + 1)
                    dq.append((n_r, n_c))



N, M = map(int, input().split()) # 행, 열
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다
bfs(0, 0)
print(maze[N - 1][M - 1])

