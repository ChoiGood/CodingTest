# 미확인 도착지
import sys
input = sys.stdin.readline
import heapq

def dijkstra(start, graph):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)

        if dist > distance[node]:
            continue

        for next_node, next_dist in graph[node]:
            new_dist = dist + next_dist

            if new_dist >= distance[next_node]:
                continue
            
            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return distance


T = int(input().rstrip()) # 테스트 케이스 수

for tc in range(1, T + 1):
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지 후보의 개수
    s, g, h = map(int, input().split()) # 출발지, g - h or h - g 를 건넘.
    g_h_dist = -1
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a, b) == (g, h) or (a, b) == (h, g):
            g_h_dist = d

    result = []
    distance_s = dijkstra(s, graph)
    distance_g = dijkstra(g, graph)
    distance_h = dijkstra(h, graph)
    for _ in range(t): # t개의 목적지 후보
        x = int(input().rstrip())
        
        if distance_s[x] != float('inf'):
            if (distance_s[g] + g_h_dist + distance_h[x] == distance_s[x]) or (distance_s[h] + g_h_dist + distance_g[x] == distance_s[x]):
                result.append(x)
    
    result.sort()
    print(*result)