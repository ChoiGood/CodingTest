# 최대 힙
import heapq
import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

hq = []

N = int(input().rstrip())

for _ in range(N):
    value = int(input().rstrip())
    
    if value == 0:
        print(0 if len(hq) == 0 else heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (-value, value))

