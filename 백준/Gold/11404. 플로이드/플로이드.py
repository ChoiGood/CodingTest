# 플로이드
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input()) # 정점의 갯수
m = int(input()) # 간선의 갯수

# 그래프 저장 : 인접 리스트
graph = [[] for _ in range(n + 1)]

# 간선 정보를 인접 리스트에 저장하기
for _ in range(m):
    a, b, c = map(int, input().split()) # a -> b 간선의 가중치 c
    graph[a].append((b, c)) # b로 가는 간선의 가중치가 c

# 모든 정점에 대해서 모든 정점의 최소 경로(비용을) 계산하는 알고리즘.
# 모든 정점 (n) 개에 대해서 모든 정점 (n)의 최단 비용을 계산..!

def floyd_warshall(graph):
    # 최단 거리를 저장할 리스트 dist, (초기화를 무한대)
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    # 초기화..
    # 1. 자기 자신으로 가는 노드의 최단 경로는 0 으로 초기화
    for i in range(n + 1):
        dist[i][i] = 0
    
    # 2. 인접리스트에 저장되어 있는 가중치 간선값으로 dist 초기화
    for v in range(n + 1):
        for u, w in graph[v]:
            dist[v][u] = min(dist[v][u], w) # v -> u 가는 간선 비용 w.

    # i -----------> j 연결하는 최단거리(비용) 계산
    #       k 라는 노드를 징검다리 역할로 부여하여 최단 거리르 갱신
    # i ---> k ---> j 로 가는 최단 거리로 갱신할 수 있다...!
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # i ----> j vs i --> k --> j 갱신!
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# import pprint
dist = floyd_warshall(graph)
# pprint.pprint(dist)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] != INF:
            print(dist[i][j], end=' ')
        else:
            print(0, end=' ')
    print()