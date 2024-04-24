# 하얀 칸
import sys
input = sys.stdin.readline

## 하얀 칸 위에 말이 몇개 있는가
def CountHorseInWhite():
    cnt = 0
    for i in range(8):
        # 조건 : 가장 왼쪽 위 칸은 하얀칸이다
        check = i % 2 # 각 줄마다 하얀칸 체크 변수 
        for j in range(8):
            if j % 2 == check and board[i][j] == 'F':
                cnt += 1
    return cnt

board = [list(input().rstrip()) for _ in range(8)]
number = CountHorseInWhite()
print(number)