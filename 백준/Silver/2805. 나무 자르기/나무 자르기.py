# 나무 자르기

def woodCalc(height):
    temp = 0
    for wood_hegith in arr:
        if wood_hegith - height > 0:
            temp += wood_hegith - height
    return temp


def findHeight(start, end):

    while start <= end:
        mid = (start + end) // 2

        wood = woodCalc(mid)

        if wood > M:
            if woodCalc(mid + 1) < M:
                return mid
            start = mid + 1
        elif wood == M:
            return mid
        else:
            end = mid - 1
    
    return 0

# 나무의 수 N, 나무의 길이 M
N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = findHeight(0, max(arr))
print(result)

