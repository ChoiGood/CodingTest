# 타임머신
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    edges.append((C, A, B))
    

# 벨만-포드 알고리즘 함수 정의
def bellman_ford(start):
    # 최단 거리를 저장할 리스트 dist, (초기화를 무한대)
    dist = [float('inf')] * (N + 1)
    # 시작 정점의 최단 거리는 0
    dist[start] = 0

    # 정점의 수 - 1 번 만큼 반복
    # + 이 이후로 추가적인 갱신을 진행하게 되었을 때! 갱신이 만약 이루어지면, 음의 사이클이 존재한다!
    for i in range(N):
        # 모든 간선의 정보를 사용하여 최단 거리르 갱신
        for w, u, v in edges:
            # start -> u 거리와 u -> v 거리의 합이
            new_dist = dist[u] + w
            # start -> v 거리보다 더 작다면...? 갱신!
            if new_dist < dist[v]:
                dist[v] = new_dist
                
                # n 번째 반복에도 값이 갱신되면 음수 순환이 존재
                if i == N - 1:
                    return False
    
    return dist # 최단 경로 리스트를 반환

# 벨만 포드 알고리즘 수행
distance = bellman_ford(1)

if distance == False:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])