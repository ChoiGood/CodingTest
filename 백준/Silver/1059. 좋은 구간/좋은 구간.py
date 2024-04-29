# 좋은 구간
import sys
input = sys.stdin.readline

L = int(input())
arr = [0] + list(map(int, input().split())) # n 을 포함해 정렬 후 n 이 arr의 최솟값 보다 작을 경우를 처리해주기 위해 0을 추가
n = int(input())

# 만약 n 이 arr에 있으면 좋은 구간이 나올 수 없다 ==> 0 출력
if n in arr:
    print(0)
else:
    # n을 넣고 정렬 수행 후 앞과 뒤의 숫자를 구하기
    arr.append(n)
    arr.sort() 
    
    x = arr.index(n)
    front = arr[x - 1]
    end = arr[x + 1]

    result = (end - n) * (n - front - 1) + (end - n - 1)
    print(result)