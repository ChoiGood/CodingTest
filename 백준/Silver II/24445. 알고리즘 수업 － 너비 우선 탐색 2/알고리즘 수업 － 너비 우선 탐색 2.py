import sys
input = sys.stdin.readline
from collections import deque

cnt = 1
def bfs(graph, node, visited):
    global cnt
    queue = deque([node])
    visited[node] = cnt
    cnt += 1
    while queue:
        v = queue.popleft()

        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = cnt
                cnt += 1

N, M, R = map(int, input().split()) # 정점의 수 N, 간선의 수 M, 시작 정점 R

graph = [[] for _ in range(N + 1)] # 그래프 정보
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse = True)

bfs(graph, R, visited)
for i in range(1, N + 1):
    print(visited[i])

