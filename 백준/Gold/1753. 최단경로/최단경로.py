# 최단 경로
# 다익스트라 구현 문제
import sys
input = sys.stdin.readline

import heapq

def dijkstra(start, graph):
    # 시작 노드로부터의 최단 거리를 저장하기 위한 distance 배열
    distance = [float('inf')] * (V + 1)
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        # start 노드 -> 검사 노드까지의 누적 거리와 현재 검사하는 노드
        dist, node = heapq.heappop(pq)
        
        # 누적 거리가 기록된 거리 보다 길다면 pass
        if dist > distance[node]:
            continue
        
        for next_node, next_dist in graph[node]:
            new_dist = dist + next_dist
            
            if new_dist >= distance[next_node]:
                continue
            
            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
            
    return distance
    
V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
K = int(input().rstrip()) # 시작 정점의 번호

graph =[[] for _ in range(V + 1)] # 인접 리스트
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = dijkstra(K, graph)

for i in range(1, V + 1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])