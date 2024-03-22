# 틀별한 최단 경로
# 특정 vertex를 걸치고 가야함!!
# 1 부터 v1, v2 순으로 N으로 가는 최단 경로와 1부터 v2, v1 순으로 거치면서 N으로 가는 경로 2가지가 존재한다.
# 최적 부분 구조를 가지므로 1~N 까지의 최단거리(v1, v2를 거치는) 를 다음과 같이 구할 수 있다.
# ex) 1 -> v2 -> v1 -> N  =>  1->v2 최단거리 + v2->v1 최단거리 + v1->N 최단거리
# v1과 v2를 거치는 1~N까지의 경로는 2가지 경우로 분류할 수 있다. (v1, v2 순으로 가는 경우, v2, v1 순으로 가는 경우)
# 1 -> v1 -> v2 -> N /// 1 -> v2 -> v1 -> N  

import heapq

def dijkstra(start, graph):
    # start 노드부터의 최단 거리를 저장하기 위한 distance 배열
    distance = [float('inf')] * (N + 1)
    distance[start] = 0 # 시작 노드 초기화
    
    pq = [(0, start)]
    
    while pq:
        # 검사 노드까지의 누적 거리, 검사 노드
        dist, node = heapq.heappop(pq)
        
        # 검사 노드까지의 누적 거리가 distance에 기록된 누적 거리보다 크면 pass (볼 필요 없다)
        if dist > distance[node]:
            continue
        
        # 노드와 인접한 노드들에 대해서 pq 에 넣어주자
        # 넣을 때 당연히 누적거리가 더 작은걸 넣는다. 
        for next_node, next_dist in graph[node]:
            # 누적거리 구하기
            new_dist = dist + next_dist
            
            # 누적 거리가 더 작으면 distance 업데이트 후 pq에 넣기
            if new_dist >= distance[next_node]:
                continue
            
            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
            
    return distance

N, E = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(N + 1)] # 인접 리스트

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())

distance_1 = dijkstra(1, graph)
distance_v1 = dijkstra(v1, graph)
distance_v2 = dijkstra(v2, graph)

path1 = distance_1[v1] + distance_v1[v2] + distance_v2[N]
path2 = distance_1[v2] + distance_v2[v1] + distance_v1[N]

result = min(path1, path2)

print(-1 if result >= float('inf') else result)