# 가장 긴 증가하는 부분 수열2

def idx_binary_search(target):
    start = 0
    end = len(lic_lst) - 1

    while start < end:
        mid = start + (end - start) // 2
        if lic_lst[mid] >= target:
            end = mid
        else:
            start = mid + 1
            
    return end

N = int(input())
arr = list(map(int, input().split()))

lic_lst = [arr[0]]
for i in range(1, N):
    if lic_lst[-1] < arr[i]:
        # 부분 수열의 마지막 값보다 넣는 수가 크면 
        # => 그대로 추가
        lic_lst.append(arr[i])
    elif lic_lst[-1] > arr[i]:
        # 들어오는 수가 부분 수열의 마지막 값보다 작으면?
        # => 해당 수 보다 작은 값중 가장 큰 값이랑 바꾸기
        idx = idx_binary_search(arr[i])
        lic_lst[idx] = arr[i] # 리스트 값 바꿔주기

print(len(lic_lst))