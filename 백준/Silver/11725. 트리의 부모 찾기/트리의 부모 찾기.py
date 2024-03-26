# 트리의 부모 찾기
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [False] * (N + 1)
    visited[start] = True # 방문처리
    dq = deque()
    dq.append((start, -1))

    while dq:
        node, prev_node = dq.popleft()

        parents[node] = prev_node # 부모 노드 정보 저장시키기 (루트는 -1)
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dq.append((next_node, node))

N = int(input())
graph = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
for i in range(2, N + 1):
    print(parents[i])
