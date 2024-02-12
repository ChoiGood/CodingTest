# 알고리즘 수업 - 깊이 우선 탐색1
# recursion 에러... => 반복문으로 구현하자!!

seq = 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(v, graph, visited):
    global seq
    visited[v] = seq
    seq += 1
    for w in graph[v]:
        if not visited[w]:
            dfs(w, graph, visited)

def dfs2(v, graph, visited):
    cnt = 1
    visited[v] = cnt
    cnt += 1
    st = []
    while True:
        for w in graph[v]:
            if not visited[w]:
                st.append(v)
                v = w
                visited[v] = cnt
                cnt += 1
                break
        else:
            if len(st) != 0:
                v = st.pop()
            else:
                break

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

i_arr = []
for _ in range(M):
    u, v  = map(int, input().split())
    i_arr.append((u, v))
    i_arr.append((v, u))

i_arr.sort()

for u, v in i_arr:
    graph[u].append(v)

dfs(R, graph, visited)

for i in range(1, N + 1):
    print(visited[i])
