from collections import deque
d_r = [-1, 1, 0, 0]
d_c = [0, 0, -1, 1]

def bfs(row, col, visited, height):
    visited[row][col] = True
    dq = deque()
    dq.append((row, col))

    while dq:
        r, c = dq.popleft()
        for d in range(4):
            n_r = r + d_r[d]
            n_c = c + d_c[d]
            if 0 <= n_r < N and 0 <= n_c < N and arr[n_r][n_c] > height and not visited[n_r][n_c]:
                visited[n_r][n_c] = True
                dq.append((n_r, n_c))


def solve():
    mx_area_num = -1
    
    for h in range(mx_height + 1):
        tmp_area_num = 0
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] > h and not visited[i][j]:
                    bfs(i, j, visited, h)
                    tmp_area_num += 1
        
        mx_area_num = max(mx_area_num, tmp_area_num)
    return mx_area_num

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mx_height = -1
for i in range(N):
    for j in range(N):
        if mx_height < arr[i][j]:
            mx_height = arr[i][j]

result = solve()
print(result)
