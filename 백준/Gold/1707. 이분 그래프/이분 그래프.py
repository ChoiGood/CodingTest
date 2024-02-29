# 이분 그래프
from collections import deque
def bfs(start, graph):
    dq = deque()
    visited[start] = 0 # 방문 처리
    dq.append(start)

    while dq:
        v = dq.popleft()

        for w in graph[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + 1 # 방문처리
                dq.append(w)
            elif visited[w] == visited[v]:
                return True
            else:
                pass
    
    return False



T = int(input()) # 테스트 케이스의 개수

for _ in range(T):
    # 입력
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [-1] * (V + 1) # 레벨 정보를 담을 거임
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for g in graph:
        g.sort()
    
    cycle = False # 싸이클 유무 판단
    for i in range(1, V + 1):
        if visited[i] == -1:
            if(bfs(i, graph)):
                cycle = True
                break
    
    print('NO' if cycle else 'YES')
