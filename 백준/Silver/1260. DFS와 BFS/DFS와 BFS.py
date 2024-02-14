# DFS와 BFS
import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w , visited)

def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True
    print(node, end = ' ')
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                print(w, end = ' ')
                queue.append(w)

# 입력
# N : 정점의 개수 (1<= N <= 1000), M : 간선의 개수 (1 <= M <= 10000), V : 탐색 시작 번호
N, M, V = map(int ,input().split()) 
# 그래프
graph = [[] for _ in range(N + 1)] 
visited1 = [False] * (N + 1) # DFS 에 쓰일 visited
visited2 = [False] * (N + 1) # BFS 에 쓰일 visited (한 번 돌리고 초기화해도 됨!!)
for _ in range(M):
    u, v = map(int, input().split()) # 입력으로 주어지는 간선은 양방향!!
    graph[u].append(v)
    graph[v].append(u)
# 정점번호가 작은 것 먼저 방문 -> 오름차순 정렬!
for g in graph:
    g.sort()
    
# 로직
dfs(graph, V, visited1)
print()
bfs(graph, V, visited2)