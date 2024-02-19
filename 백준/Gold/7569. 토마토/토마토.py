# 토마토 3 차원
from collections import deque
import sys
input = sys.stdin.readline

d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

def bfs(st_lst):
    dq = deque()
    for z, x, y in st_lst:  # 방문처리
        arr[z][x][y] = 1 
        dq.append((z, x, y))
    
    while dq:
        z, x, y = dq.popleft()
        for dz, dx, dy in d:
            n_z, n_x, n_y= z + dz, x + dx, y + dy
            
            if 0 <= n_z < H and 0 <= n_x < N and 0 <= n_y < M: # 상자 안이고
                if arr[n_z][n_x][n_y] == 0: # 갈 수 있으면
                    arr[n_z][n_x][n_y] = arr[z][x][y] + 1   # 방문처리
                    dq.append((n_z, n_x, n_y))



M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

st_lst = [] # 시작점들의 위치
for i in range(N):
    for j in range(M):
        for k in range(H):
            if arr[k][i][j] == 1:
                st_lst.append((k, i, j))

bfs(st_lst)

tomatoLeft = False
mn_day = 0
for i in range(N):
    for j in range(M):
        for k in range(H):
            if arr[k][i][j] == 0:
                tomatoLeft = True
            if mn_day < arr[k][i][j]:
                mn_day = arr[k][i][j] 

print(-1 if tomatoLeft else mn_day - 1)