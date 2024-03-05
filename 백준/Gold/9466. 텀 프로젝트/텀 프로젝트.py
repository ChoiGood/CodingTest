# 텀 프로젝트
import sys
sys.setrecursionlimit(10 ** 7)

def findTeam(person):
    global team_cnt
    visited[person] = True
    path.add(person) # 현재 나의 경로를 표현하기 위함
    if not visited[graph[person]]:
        findTeam(graph[person])
    else: # 방문한적이 있는 아이들이다
        # 1. 싸이클인 경우 => 팀의 개수 올려주기
        # 2. 다음 dfs 탐색에서 해당 노드가 이미 방문한 그래프(팀 개수가 처리된)를 가르키는 경우 => 무시
        # 이 두가지 케이스를 구분해줘야함..!!
        if graph[person] in path: # 싸이클인 경우 (내 경로상에 다음 노드가 있는 경우)
            # 싸이클 발견 => 팀 개수에 정해주기
            next_person = graph[person]
            while next_person != person:
                team_cnt += 1
                next_person = graph[next_person]
            team_cnt += 1
T = int(input())
for _ in range(T):
    N = int(input())
    graph = list(map(int, input().split()))
    graph.insert(0, 9999999)

    visited = [False] * (N + 1)
    path = set()

    team_cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            path.clear()
            findTeam(i)

    print(N - team_cnt)