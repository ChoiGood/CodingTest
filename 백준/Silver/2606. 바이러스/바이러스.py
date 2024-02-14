# 바이러스
import sys
input = sys.stdin.readline

from collections import deque

# dfs 로 탐색
def dfs(graph, v, visited):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited)

# bfs 로 탐색
def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True

# 입력
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 로직
# dfs(graph, 1, visited)
bfs(graph, 1, visited)

# 출력 : 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번을 통해 바이러스에 걸리게 되는 컴퓨터의 수 출력
cnt = 0
for i in range(2, n + 1):
    if visited[i]:
        cnt += 1
print(cnt)