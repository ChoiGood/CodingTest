# # 공유기 설치

# # 이진 탐색
# # !! 정렬된 배열에서만 사용할 수 있다
# # 배열 내부의 데이터가 정렬되어 있어야 사용 가능한 알고리즘이다
# # 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다
#     # 변수 3개 = 시작점, 끝점, 중간점
#     # 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하여 원하는 데이터를 찾는다.

# # 한번 확인할 때마다 확인하는 원소의 개수가 절반씩 주어든다!
# # 시간 복잡도 : O(logN)

# # 재귀함수로 구현한 이진 탐색
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2

#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
    
# n, target = map(int, input().split())
# array = list(map(int, input().split()))

# # 반복문으로 구현한 이진 탐색
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid -1
#         else:
#             start = mid + 1

#     return None

# result = binary_search(array, target, 0, n - 1)
# if result is None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)


# # Lower Bound & Upper Bound
    
# # Lower bound 는 데이터 내에서 특정 값보다 같거나 큰 값이 처음 나오는 위치를 리턴해준다.
# # 파이썬 bisect 모듈의 bisect_left

# def lower_bound(data, target):
#     lo = 0
#     hi = len(data)
#     while lo < hi:
#         mid = (lo + hi) // 2
#         if target <= data[mid]:
#             hi = mid
#         else:
#             lo = mid + 1
        

import sys
input = sys.stdin.readline

def lanCount(dist):
    tmp_cnt = 1
    prev = homes[0]
    # 조건 확인하기
    for i in range(1, N):
        if homes[i] - prev >= dist:
            tmp_cnt += 1
            prev = homes[i]

    return tmp_cnt

# 집의 개수 N, 공유기의 개수 C
N, C = map(int, input().split())
homes = []
for _ in range(N):
    x = int(input().rstrip())
    homes.append(x)

# 1. 집들의 좌표를 정렬하기
homes.sort()

# 2. 집들 사잉의 거리르 초기화하기
# 최소거리 1, 최대 거리 마지막 집 - 첫 번째 집으로 초기화하기
# 거리(설치된 공유기 사이의 최대거리)를 이용하여 이분 탐색을 진행하기 위함

start = 1
end = homes[N - 1] - homes[0]
result = 0

# 3. 이분 탐색 (매개변수 탐색) 진행
while start <= end:
    mid = (start + end) // 2
    
    # 해당 거리(mid) 로 설치 가능한 공유기의 수
    cnt = lanCount(mid)

    # 공유기를 제한 갯수 이상 사용했을 경우, 공유기 사이의 거리를 늘리고 다시 설치
    if cnt >= C:
        result = max(result, mid)
        start = mid + 1
    else:
    # 공유기를 제한 개수 미만으로 사용했을 경우, 공유기를 사이의 거리를 좁히고 다시 설치
        end = mid - 1

print(result)

