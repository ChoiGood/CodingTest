# 치킨 배달
import sys
from collections import deque
input = sys.stdin.readline

d_r = [-1, 1, 0, 0]
d_c = [0, 0, -1, 1]

def bfs(start_lst):
    # 해당 도시에서 치킨집가는 최단거리 구현하기
    visited = [[-1] * N for _ in range(N)]
    dq = deque()
    for row, col in start_lst:
        visited[row][col] = 0 # 방문처리
        dq.append((row, col))
        
    while dq:
        r, c = dq.popleft()
        for d in range(4):
            n_r, n_c = r + d_r[d], c + d_c[d]
            if 0 <= n_r < N and 0 <= n_c < N and visited[n_r][n_c] == -1:
                dq.append((n_r, n_c))
                visited[n_r][n_c] = visited[r][c] + 1

    return visited

mn_dist = 99999999999
def dfs(d, chicken):
    global mn_dist
    if len(chicken) == M:
        result = bfs(chicken)
        
        dist = 0
        for row, col in houses:
            dist += result[row][col]

        mn_dist = min(mn_dist, dist)
        return
    if d >= H:
        return

    # 포함하는 경우
    chicken.append(foodseller[d])
    dfs(d + 1, chicken)
    chicken.pop()

    # 포함하지 않는 경우
    dfs(d + 1, chicken)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

houses = []
foodseller = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            foodseller.append((i, j))
        if arr[i][j] == 1:
            houses.append((i, j))
            
H = len(foodseller)

dfs(0, [])

print(mn_dist)
