# 수 찾기
# 1초 n, m 100000  => 이진 탐색
# 시간 복잡도 : nlog(n) (정렬) + mlog(n) (숫자 m번 찾기)
def binarySearch(start, end, search_num, A):
    
    while start <= end:
        mid = (start + end) // 2

        if A[mid] == search_num:
            return 1
        elif A[mid] > search_num:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
search_nums = list(map(int, input().split()))

for num in search_nums:
    print(binarySearch(0, N - 1, num, arr))

