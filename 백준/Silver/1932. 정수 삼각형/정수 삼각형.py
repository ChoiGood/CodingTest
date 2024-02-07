import copy

# 정수 삼각형
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

S = copy.deepcopy(arr)


# 초기화 (기저상태 만들기)
for i in range(1, N):
    S[i][0] += S[i - 1][0]
for i in range(1, N):
    S[i][i] += S[i - 1][i - 1]

# Bottom - Up 으로 구현
for i in range(2, N):
    for j in range(1, i): # j : 0 -> i (끝)  처음과 끝은 빼 => j : 1 -> i - 1
        S[i][j] += max(S[i - 1][j - 1], S[i - 1][j])

print(max(S[N - 1]))
