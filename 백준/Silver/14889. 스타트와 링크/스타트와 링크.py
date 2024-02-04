# import sys
# input = sys.stdin.readline

# balance = 99999999
# def decideTeam(d, N, members, m_check, S):
#     '''
#     d : 깊이
#     N : 축구선수 수 (짝수)
#     members : 팀 멤버 리스트
#     S : 선수간 시너지 정보
#     '''
#     if d == N // 2:
#         global balance

#         others = [i for i in range(1, N + 1) if (i not in members)]
     
#         teamA = 0
#         for i in range(N // 2 - 1):
#             for j in range(i + 1, N // 2):
#                 teamA += S[members[i]][members[j]]
#                 teamA += S[members[j]][members[i]]

#         teamB = 0
#         for i in range(N // 2 - 1):
#             for j in range(i + 1, N // 2):
#                 teamB += S[others[i]][others[j]]
#                 teamB += S[others[j]][others[i]]

#         tmp_bal = abs(teamA - teamB)
#         if balance > tmp_bal:
#             balance = tmp_bal

#     else:
#         for i in range(1, N + 1):
#             if not m_check[i]:
#                 members.append(i)
#                 m_check[i] = True
#                 decideTeam(d + 1, N, members, m_check, S)
#                 members.pop()
#                 m_check[i] = False


# N = int(input())

# S = [list(map(int, input().split())) for _ in range(N)]

# for a in S:
#     a.insert(0, 0)
# S.insert(0, [0] * (N + 1))
# m_check = [False] * (N + 1)
# m_check[1] = True

# decideTeam(1, N, [1], m_check, S)

# print(balance)

import sys
input = sys.stdin.readline
bal = 99999999999999
def dfs(d, idx):
    if d == N // 2:
        global bal
        teamA = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    teamA += S[i][j]
        teamB = 0
        for i in range(N):
            for j in range(N):
                if (not visited[i]) and (not visited[j]):
                    teamB += S[i][j]
        
        bal = min(bal, abs(teamA - teamB))
        
    else:
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = True
                dfs(d + 1, i + 1)
                visited[i] = False




N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * (N)
visited[0] = True
dfs(1, 1)

print(bal)