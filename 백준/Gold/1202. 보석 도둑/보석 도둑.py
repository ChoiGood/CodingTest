# 보석 도둑
import sys
import heapq
input = sys.stdin.readline

# 보석의 개수, 가방의 개수
n, k = map(int, input().split())
# 보석의 정보 (무게, 가격)
jewel_lst = [tuple(map(int, input().split())) for _ in range(n)]
# 가방의 정보 (무게)
bag_lst = [int(input()) for _ in range(k)]

# 오름차순 정렬하기
jewel_lst.sort(key = lambda x: (x[0], -x[1]))
bag_lst.sort()
# 가방의 무게에 따라 훔칠수 있는 최고가치의 보석을 뽑아주기 위한 pq
pq = []
mx_value = 0
for bag in bag_lst:
    while jewel_lst and jewel_lst[0][0] <= bag:
        heapq.heappush(pq, (-jewel_lst[0][1], jewel_lst[0][1]))
        heapq.heappop(jewel_lst)
    if pq:
        mx_value += heapq.heappop(pq)[1]
print(mx_value)