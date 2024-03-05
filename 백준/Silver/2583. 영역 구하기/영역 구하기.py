# 영역 구하기
from collections import deque

# 상하좌우를 위한 델타리스트
d_r = [-1, 1, 0, 0]
d_c = [0, 0, -1, 1]

def bfs(row, col):
    dq = deque()
    dq.append((row, col))
    visited[row][col] = True # 방문 처리

    area = 0 # 영역의 넓이

    while dq:
        r,c = dq.popleft()
        area += 1
        for d in range(4):
            n_r = r + d_r[d]
            n_c = c + d_c[d]
            if 0 <= n_r < M and 0 <= n_c < N and not visited[n_r][n_c]:
                visited[n_r][n_c] = True # 방문처리
                dq.append((n_r, n_c))
    return area

M, N, K = map(int, input().split())
# arr = [[0] * M for _ in range(N)]
visited = [[False] * N for _ in range(M)]

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            # arr[i][j] += 1
            visited[i][j] = True

cnt = 0
result = []
for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
            cnt += 1
            result.append(bfs(i, j))
result.sort()

print(cnt)
print(*result)
