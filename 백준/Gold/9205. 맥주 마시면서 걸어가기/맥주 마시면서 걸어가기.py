# 맥주 마시면서 걸어가기
from collections import deque
import sys
input = sys.stdin.readline

def manhaton(mypos, target):
    return abs(mypos[0] - target[0]) + abs(mypos[1] - target[1])

def bfs(start):
    visited = [False] * (n + 2)
    visited[start] = True # 방문 처리
    dq = deque()
    dq.append(start)

    while dq:
        current = dq.popleft()
        if current == n + 1: # 목적지에 도달했다면
            return 'happy'

        for i in range(n + 2):
            if not visited[i] and manhaton(graph[current], graph[i]) <= 1000:
                visited[i] = True
                dq.append(i)
    return 'sad'
        
t = int(input()) # 테스트 케이스 수

for _ in range(t):
    n = int(input().rstrip()) # 편의점 개수
    graph = [] # 좌표 정보

    for i in range(n + 2):
        x, y = map(int, input().rstrip().split())
        graph.append((x, y)) # x좌표 y좌표

    result = bfs(0)
    print(result)
