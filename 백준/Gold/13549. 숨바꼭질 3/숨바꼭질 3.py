import heapq

L = 100001

# 다익스트라 구현
def dijkstra(start):
    time_info = [float('inf')] * L
    time_info[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        cur_time, node = heapq.heappop(pq)
        
        if cur_time > time_info[node]:
            continue
        
        for next_time, next_node in [(1, node - 1), (1, node + 1), (0, 2*node)]:
            if 0 <= next_node < L:
                new_time = cur_time + next_time
                
                if new_time >= time_info[next_node]:
                    continue
                
                time_info[next_node] = new_time
                heapq.heappush(pq, (new_time, next_node))
                
    return time_info
    

N, K = map(int, input().split())
time_info = dijkstra(N)

print(time_info[K])
