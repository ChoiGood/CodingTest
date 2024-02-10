# 랜선 자르기
import sys
input = sys.stdin.readline

def lenthCount(arr, lenth):
    tmp = 0
    for value in arr:
        tmp += value // lenth
    return tmp

def binarySearch(arr, search_num):
    # arr 의 제일 큰 값에서 부터 쭈욱 서치하면서
    # 랜선의 개수가 N이 되게 해주는 값을 찾기
    start = 1
    end = arr[-1]

    result = 1
    while start <= end:
        mid = (start + end) // 2

        # 체크 로직
        tmp = lenthCount(arr, mid)

        if tmp > search_num: # 랜선의 개수가 찾는 값보다 크면 ==> 랜선의 개수를 작게!! -> mid 값이 커져야함
            result = mid
            start = mid + 1
        elif tmp < search_num:
            end = mid - 1
        else:
            if lenthCount(arr, mid + 1) < search_num:
                result = mid
                break
            else:
                start = mid + 1

    # result 에는 현재 랜선의 개수를 N 개를 만들 수 있는 길이가 담겨 있음!!!! -> 이를 이제 하나씩 늘려가며 최댓값을 찾아 주자!!!    
    while True:
        result += 1
        
        tmp = 0
        for value in arr:
            tmp += value // result
        
        if tmp < search_num:
            break
    result -= 1

    return result

K, N = map(int, input().split())

arr = []
for _ in range(K):
    tmp = int(input())
    arr.append(tmp)
arr.sort()

result = binarySearch(arr, N)
print(result)