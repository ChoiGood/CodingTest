import sys
input = sys.stdin.readline
from collections import deque
def bfs(start):
    visited = [False] * (V + 1)
    visited[start] = True # 방문 처리
    dq = deque()
    dq.append((start, 0)) # 정점, 누적 거리

    mx_dist = -1
    mx_node = -1

    while dq:
        node, dist = dq.popleft()

        if mx_dist < dist:
            mx_dist = dist
            mx_node = node

        for next_node, next_dist in graph[node]:
            if not visited[next_node]:
                # 누적 거리 구하기
                new_dist = dist + next_dist
                
                visited[next_node] = True
                dq.append((next_node, new_dist))
    
    return mx_node, mx_dist

V = int(input().rstrip()) # 정점의 개수
graph = [[] for _ in range(V + 1)] # 그래프(트리) 정보
for _ in range(V):
    s, *arr, tmp = map(int, input().split()) # 정점 번호, 연결된 간선의 정보, 종료값 -1
    for i in range(0, len(arr), 2):
        graph[s].append((arr[i], arr[i+1]))

# 로직
# 임의의 정점 x 에서의 최장 거리를 가진 정점 y를 구한다.
# 그 y로부터 최장거리를 구하면 그것이 트리의 지름이 된다.
# 증명 : 귀류법 (생략)

y, dist = bfs(1)
temp, result = bfs(y)

print(result)