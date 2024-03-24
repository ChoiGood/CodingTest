import sys
input = sys.stdin.readline
# import heapq
# 최소신장트리를 구하는 알고리즘
# 1. 프림 알고리즘 : 
# 한 노드를 선택하고
# 인접한 노드들을 가중치가 낮은 순으로 검사하면서 (bfs + priority queue)
# cycle이 생기지 않으면 신장 트리에 추가

# 2. 크루스칼 알고리즘:
# 모든 간선 정보를 저장하고
# 가중치를 기준으로 오름차순 정렬
# 가중치가 낮은 순으로 간선들을 검사하면서 최소비용 신장 트리에 추가
# 해당 간선을 추가할 때 cycle 이 생성된다면 추가하지 않는다 (cycle 검사를 union-find 알고리즘으로 처리)
# V - 1 개의 간선을 선택하면 => 최소 비용 신장 트리 완성

# def prim(start):
#     visited = [False] * (N + 1)
#     pq = [(0, start)]
#     weight_sum = 0

#     while pq:
#         weight, node = heapq.heappop(pq)

#         # 우선순위 큐를 쓰기 떄문에 미리 pq 에 (가중치가 높은)들어간 노드들이 (가중치가 낮은 걸로) 연결이 된 상태라면 pass 
#         if visited[node]:
#             continue
        
#         # 최소 신장 트리에 추가
#         visited[node] = True # 방문 처리
#         weight_sum += weight

#         for next_node, w in graph[node]:
#             # 싸이클이 만들어지는 경우 pass
#             if visited[next_node]:
#                 continue
#             heapq.heappush(pq, (w, next_node))
    
#     return weight_sum
        
# N = int(input().rstrip()) # 컴퓨터의 수 (노드)
# M = int(input().rstrip()) # 연결할 수 있는 선의 수 (간선)

# graph = [[] for _ in range(N + 1)]
# for _ in range(M):
#     s, e, w = map(int, input().split())
#     graph[s].append((e, w))
#     graph[e].append((s, w))

# result = prim(1)
# print(result)

def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

N = int(input().rstrip()) # 컴퓨터의 수 (노드)
M = int(input().rstrip()) # 연결할 수 있는 선의 수 (간선)

edges = []
parents = list(range(N + 1))

for _ in range(M):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))

edges.sort() # 가중치를 기준으로 오름 차순 정렬
cnt = 0 # 최소비용 신장트리의 간선의 개수 : V - 1 
weight_sum = 0

for w, s, e in edges: 
    # Cycle이 생기면 pass <= 노드 s, e 가 같은 집합에 있다면 cycle이 생성됨
    # union-find 알고리즘을 활용해 Cycle 여부를 판단하자
    root_s = find_set(s)
    root_e = find_set(e)

    # Cycle이 생성되는 경우 pass
    if root_s == root_e:
        continue
    
    # 해당 간선을 최소비용신장 트리에 추가
    cnt += 1
    weight_sum += w
    # union 과정
    if root_s < root_e:
        parents[root_e] = root_s
    else:
        parents[root_s] = root_e
    
print(weight_sum)
