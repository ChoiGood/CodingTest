# 여행 가자
import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for w in range(1, N + 1):
        if graph[v][w] == 1 and not visited[w]:
            dfs(w)

# 인접 행렬로 구현
# 1. 완전 탐색으로 풀이 (dfs)

N = int(input())
M = int(input())

visited = [False] * (N + 1)
graph = [[-1] + list(map(int, input().split())) for _ in range(N)]
graph.insert(0, [-1] * (N + 1))

arr = list(map(int, input().split()))

dfs(arr[0])
flag = True
for node in arr:
    if visited[node] == False:
        flag = False
        break

print('YES' if flag else 'NO')


