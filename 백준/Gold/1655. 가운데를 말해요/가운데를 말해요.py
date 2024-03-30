# 가운데를 말해요
import sys
input = sys.stdin.readline
import heapq

N = int(input().rstrip())

# 모래시계 처럼 구현
mn_heap = []
mx_heap = []

for _ in range(N):
    x = int(input().rstrip())

    # max_heap 의 개수가 mn_heap과 같거나 1개 더 많게 유지시키자!!
    if len(mn_heap) < len(mx_heap):
        # mn_heap에 넣어주기
        heapq.heappush(mn_heap, (x, x))
    else:
        # mx_heap에 넣어주기
        heapq.heappush(mx_heap, (-x, x))

    # 만약 mn_heap 의 top 값이 max_heap의 top 값보다 더 작다면 swap
    if len(mn_heap) != 0 and mn_heap[0][1] < mx_heap[0][1]:
        temp1, x = heapq.heappop(mn_heap)
        temp2, y = heapq.heappop(mx_heap)

        heapq.heappush(mn_heap, (y, y))
        heapq.heappush(mx_heap, (-x, x))

    print(mx_heap[0][1])