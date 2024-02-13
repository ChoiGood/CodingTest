# 깊이 우선 탐색 2

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

cnt = 1
def dfs(v, graph, visited):
    global cnt
    visited[v] = cnt
    cnt += 1
    for w in graph[v]:
        if visited[w] == 0:
            dfs(w, graph, visited)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse = True)

dfs(R, graph, visited)

for i in range(1, N + 1):
    print(visited[i])