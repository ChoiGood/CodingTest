# 치즈

# 1초 후 처리
# 1. (0,0) 에서 시작하는 bfs를 돌리며 공기중을 visited 처리함.
# 2. 배열을 순회하면서 치즈 상하좌우에 공기가 있으면 치즈 없애기
# 이를 반복하며 구현한다.
d_r = [-1, 1, 0, 0]
d_c = [0, 0, -1, 1]

from collections import deque
def bfs(row, col):
    visited = [[False] * M for _ in range(N)]
    visited[row][col] = True # 방문처리
    dq = deque()
    dq.append((row, col))

    melting = []

    while dq:
        r, c = dq.popleft()

        for d in range(4):
            n_r = r + d_r[d]
            n_c = c + d_c[d]
            if 0 <= n_r < N and 0 <= n_c < M and not visited[n_r][n_c]: # 범위 안이고, 방문하지 않았 곳
                # 공기면
                if arr[n_r][n_c] == 0:
                    visited[n_r][n_c] = True # 방문처리
                    dq.append((n_r, n_c))
                else: # arr[n_r][n_c] == 1
                    # 가장 바깥쪽의 치즈들에 대한 처리
                    visited[n_r][n_c] = True
                    melting.append((n_r, n_c))

    # 가장 바깥쪽의 치즈들 녹이기!!
    for r, c in melting:
        arr[r][c] = 0




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 초기 치즈 개수
cnt = 0
for i in range(N):
    cnt += arr[i].count(1)

t = 0
while True:
    # 이전의 치즈 개수 저장하기
    temp_cnt = cnt

    # bfs를 돌며 치즈 시뮬레이션
    t += 1
    bfs(0, 0)

    # 남아있는 치즈개수 세아리기
    cnt = 0
    for i in range(N):
        cnt += arr[i].count(1)

    if cnt == 0:
        break

print(t)
print(temp_cnt)



