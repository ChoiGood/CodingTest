# 주사위 게임
import sys
input = sys.stdin.readline

def Game(a, b, c):
    dice = set((a, b, c))

    # 같은 눈이 3개인 경우
    if len(dice) == 1:
        money = 10000 + a * 1000
    # 같은 눈이 2개인 경우
    elif len(dice) == 2:
        same = a if a == b or a == c else b
        money = 1000 + same * 100
    # 전부 다른 눈인 경우
    else: # len(dice) == 3:
        money = max(a, b, c) * 100
    
    return money
      
N = int(input())

mx_money = -1
for _ in range(N):
   a, b, c = map(int, input().split())
   money = Game(a, b, c)
   mx_money = max(mx_money, money)

print(mx_money)