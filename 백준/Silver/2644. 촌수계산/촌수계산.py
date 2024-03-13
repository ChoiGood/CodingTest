# 촌수계산
from collections import deque
def bfs(start, end):
    visited = [0] * (n + 1) # 촌수 계산을 위한 visited
    visited[start] = 0 # 방문 처리
    dq = deque()
    dq.append(start)

    while dq:
        v = dq.popleft()
        if v == end:
            return visited[v]
        
        for w in graph[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                dq.append(w)    
    return -1

n = int(input()) # 전체 사람의 수 n
x, y = map(int, input().split()) # 촌수를 계산해야 하는 두 사람의 번호
graph = [[] for _ in range(n + 1)]

m = int(input()) # 관계의 개수
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

result = bfs(x, y)
print(result)