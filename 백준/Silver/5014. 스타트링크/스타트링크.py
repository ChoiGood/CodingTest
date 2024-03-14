# 스타트링크
from collections import deque

def bfs(start):
    visited = [-1] * (F + 1)
    visited[start] = 0 # 시작위치 방문 처리 
    dq = deque()
    dq.append(start)

    while dq:
        c_p = dq.popleft()
        if c_p == G:
            return visited[c_p]
        
        for d in [-D, U]:
            n_p = c_p + d
            if 1 <= n_p <= F and visited[n_p] == -1: # 갈 수 있는 층이고 방문하지 않은 층이면
                visited[n_p] = visited[c_p] + 1
                dq.append(n_p)
    
    return 'use the stairs'

# F층으로 이루어진 건물 : 출발지 S 층 -> 도착지 G 층으로 버튼 당 U 층 위 이동, D 층 아래 이동
# BFS로 최단거리 구하기!!
F, S, G, U, D = map(int, input().split())
result = bfs(S)
print(result)