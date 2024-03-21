# 카드 정렬하기

# 제일 처음든 생각 -> dp??
# but... N : 100,000  내가 생각한 dp 풀이는 O(N^2 / 2)
# 따라서 다른 알고리즘 접근법을 생각해야했음..!!

# 다시 생각해보니 그리디로 해결가능!! => O(N)
# 먼저 계산되는 카드 뭉치는 쌓여서 다음 카드 비교 연산에 더해진다.
# 따라서 제일먼저 계산되는 카드뭉치를 가장 작게 만들어 줘야한다.
# ==> priority queue를 사용하자

import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    heapq.heappush(pq, int(input().rstrip()))

compare_cnt = 0 # 비교 횟수

for _ in range(N - 1):
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    compare_cnt += a + b
    heapq.heappush(pq, a + b)

print(compare_cnt)