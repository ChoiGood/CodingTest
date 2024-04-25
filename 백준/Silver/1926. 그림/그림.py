# 그림
import sys
input = sys.stdin.readline
from collections import deque

dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(s_row, s_col):
    visited[s_row][s_col] = True # 방문처리
    dq = deque()
    dq.append((s_row, s_col))
    area = 0 # 그림의 넓이

    while dq:
        c_row, c_col = dq.popleft()
        area += 1

        for d_r, d_c in dt:
            n_row = c_row + d_r
            n_col = c_col + d_c

            # 범위 안이고 그림이 있고 방문하지 않았다면
            if 0 <= n_row < n and 0 <= n_col < m and not visited[n_row][n_col] and arr[n_row][n_col] == 1:
                visited[n_row][n_col] = True # 방문 처리
                dq.append((n_row, n_col)) # dq에 추가
    
    return area


# 세로 크기 n, 가로 크기 m
n, m = map(int, input().split()) 

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt = 0 # 그림의 개수
mx_area = 0 # 가장 넓은 그림의 넓이
for i in range(n):
    for j in range(m):
        # 방문하지 않았고 그림 (탐색)을 시작할 수 있으면
        if not visited[i][j] and arr[i][j] == 1:
            cnt += 1
            tmp_area = bfs(i, j)
            mx_area = max(mx_area, tmp_area)

print(cnt)
print(mx_area)