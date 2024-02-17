# 숨바꼭질
from collections import deque
def bfs(start):
    path[start] = 0 # 방문처리 (시작 지점은 0초)
    dq = deque()
    dq.append(start)

    while dq:
        x = dq.popleft()
        for next in [x - 1, x + 1, 2 * x]:
            if 0 <= next < PATH_MAX and path[next] == -1:
                path[next] = path[x] + 1 # 방문처리
                dq.append(next)

                if next == K: # 도착 지점에 도달하면 stop!
                    return path[K]
 
PATH_MAX = 100001
N, K = map(int, input().split())
path = [-1] * PATH_MAX

bfs(N)

print(path[K])