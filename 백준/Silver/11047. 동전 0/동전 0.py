import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

coins.reverse()

cnt = 0
while K > 0:
    tmp_coin = 0
    for coin in coins:
        if coin <= K:
            tmp_coin = coin
            break
    
    cnt += (K // tmp_coin)
    K %= tmp_coin

print(cnt)