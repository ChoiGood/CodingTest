from collections import deque
import sys
import copy
input = sys.stdin.readline


d_r = [-1, 1, 0, 0]
d_c = [0, 0, -1, 1]

def bfs(start_lst):
    dq = deque()
    for row, col in start_lst:    
        arr[row][col] = 1 # 방문처리
        dq.append((row, col))

    while dq:
        r, c = dq.popleft()

        for d in range(4):
            n_r = r + d_r[d]
            n_c = c + d_c[d]
            if 0 <= n_r < N and 0 <= n_c < M and arr[n_r][n_c] == 0:
                day = arr[r][c] + 1
                arr[n_r][n_c] = day # 방문처리
                dq.append((n_r, n_c))



M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

start_lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            start_lst.append((i, j))

bfs(start_lst)

tomato_rear = False
mn_day = 0
for i in range(N):
    end = False
    for j in range(M):
        if arr[i][j] == 0:
            tomato_rear = True
            end = True
            break
        if mn_day < arr[i][j]:
            mn_day = arr[i][j]
    if end:
        break

# if tomato_rear:
#     print(-1)
# else:
#     print(mn_day)

print(-1 if tomato_rear else mn_day - 1)