# 두 수의 합
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# 투 포인터 알고리즘
arr.sort()
i = 0
j = n - 1
cnt = 0
while i < j:
    value = arr[i] + arr[j]

    if value == x:
        i += 1
        j -= 1
        cnt +=1
    elif value > x:
        j -= 1
    else: # value < x:
        i += 1

print(cnt)