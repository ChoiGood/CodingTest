import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

def dfs(row, col):
    arr[row][col] = 0 # 방문처리

    for d in range(4):
        n_r = row + d_row[d]
        n_c = col + d_col[d]

        if 0 <= n_r < N and 0 <= n_c < M and arr[n_r][n_c] >= 1:
            dfs(n_r, n_c)


# 유기농 배추
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split()) # 가로길이, 세로길이, 배추 개수

    arr = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)