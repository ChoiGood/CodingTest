# 뱀과 사다리 게임
# 게임의 목표 1번 칸 -> 100번 칸
# 사다리 수 N, 뱀의 수 M
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [-1] * 101
    dq = deque()
    visited[start] = 0 # 방문처리
    dq.append(start)

    while dq:
        node = dq.popleft()

        # 그래프 정보
        for i in range(1, 7): # 주사위 이동
            next_node = node + i

            if next_node in ladder: # 도착한 칸이 사다리면 타고 올라간다
                next_node = ladder[next_node]
                if visited[next_node] == -1: # 방문하지 않은 노드라면
                    visited[next_node] = visited[node] + 1 # 방문처리
                    dq.append(next_node)
                
                if next_node == 100:
                    return visited[100]
                continue
            if next_node in snake: # 도착한 칸이 사다리면 타고 올라간다
                next_node = snake[next_node]
                if visited[next_node] == -1: # 방문하지 않은 노드라면
                    visited[next_node] = visited[node] + 1 # 방문처리
                    dq.append(next_node)
                
                if next_node == 100:
                    return visited[100]
                continue

            if visited[next_node] == -1: # 방문하지 않은 노드라면
                visited[next_node] = visited[node] + 1 # 방문 처리 : 이동 횟수 누적시키기
                dq.append(next_node)

                if next_node == 100: # 100 (도착점)에 도달하면 종료
                    return visited[100]
        
N, M = map(int, input().split())
ladder = {}
snake = {}

# 사다리 정보
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

# 뱀 정보
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

print(bfs(1))