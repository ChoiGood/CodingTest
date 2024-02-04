#  체스판 다시 칠하기2
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
Board = [list(input()) for _ in range(N)]

def makeChess(color):
    colorChange = {'B':'W', 'W':'B'}
    arr = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        tmp = color
        for j in range(M):
            if Board[i][j] != tmp:
                arr[i + 1][j + 1] += 1
            tmp = colorChange[tmp]
        color = colorChange[color]

    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            arr[i][j] = arr[i][j] + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

    return arr

chessB = makeChess('B') 
chessW = makeChess('W')

# for a in chessB:
#     print(*a)
# for b in chessW:
#     print(*b)

best_min = 9999999999999999999
for i in range(1, N - K + 2):
    for j in range(1, M - K + 2):
        cntB = chessB[i + K - 1][j + K - 1] - chessB[i - 1][j + K - 1] - chessB[i + K - 1][j - 1] + chessB[i - 1][j - 1]
        cntW = chessW[i + K - 1][j + K - 1] - chessW[i - 1][j + K - 1] - chessW[i + K - 1][j - 1] + chessW[i - 1][j - 1]
        best_min = min(best_min, cntB, cntW)

print(best_min)


# N = 2000... => 배열을 순회하면서 K2 만큼 검사하면 시간초과!!!
# 검사를 O(n2) -> O(1) 로 줄여야한다!! => 생각을 다양하게 하자...
# 이 방법을 누적합으로!!

# 배열을 꼭 순회할 필요 없구나... !!
# B와 W 기준으로 틀린 부분을 count 하고 누적합해주면 됨!!!

