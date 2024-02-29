# 최대 힙
import sys
import heapq

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    value = int(input().rstrip())
    if value == 0:
        print(0 if len(hq) == 0 else heapq.heappop(hq))
    else:
        heapq.heappush(hq, value)