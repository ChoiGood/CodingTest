# 연료 채우기
import heapq


N = int(input()) # 주유소의 개수

oils_info = []
for i in range(1, N + 1):
    # 시작 위치에서 주유소 까지의 거리, 그 주유소에서 채울 수 있는 연료의 양
    a, b = map(int, input().split())
    oils_info.append((a, b))

# 성경이의 위치에서 마을까지의 거리, 트럭에 원래 있던 연료의 양
L, P = map(int, input().split())
oils_info.append((L, 0))

oils_info.sort() # 거리 순으로 정렬
pq = [] # 채울 수 있는 연료가 많은 순으로 max_heap 생성.

reached_dist = P # 현재 내가 도달 가능한 거리
cnt = 0
result = -1

for dist, fuel in oils_info:
    # 마을에 도달 할 수 있으면 종료
    if reached_dist >= L:
        result = cnt
        break
    # 현재 내가 도달할 수 있는 거리라면
    if reached_dist >= dist:
        # pq 안에 넣기
        heapq.heappush(pq, (-fuel, dist, fuel))
    # 현재 내가 도달할 수 있는 거리가 아니라면
    else:
        # pq가 비어있지 않으면 -> heappop 하면서 reached_dist >= dist 까지 늘리기 
        while len(pq) != 0 and reached_dist < dist:
            reached_dist += heapq.heappop(pq)[2]
            cnt += 1

        # 도달 불가능한 경우... 종료
        if reached_dist < dist:
            break
        # 도달 가능한 경우... 다시 pq에 넣고 진행하기
        else:
            heapq.heappush(pq, (-fuel, dist, fuel))
    
    if reached_dist >= L:
            result = cnt
            break

print(result)