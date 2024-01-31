def merge_sort(A, p, r): # A[p..r]을 오름차순 정렬한다.
    if p < r:
        q = (p + r) // 2       # q는 p, r의 중간 지점
        merge_sort(A, p ,q)     # 전반부 정렬
        merge_sort(A, q + 1, r) # 후반부 정렬
        merge(A, p, q, r)       # 병합

# A[p..q]와 A[q+1..r] 을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r] 은 이미 오름차순으로 정렬되어 있다.
cnt = 0
global k_value

def merge(A, p, q, r):
    global cnt
    global k_value
    global tmp

    i, j, t = p, q + 1, 1
    while i <= q and j <= r :
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1
    while i <= q: # 왼쪽 배열 부분이 남은 경우
        tmp[t] = A[i]
        t += 1
        i += 1
    while j <= r: # 오른쪽 배열 부분이 남은 경우
        tmp[t] = A[j]
        t += 1
        j += 1
    i, t = p, 1

    while i <= r: # 결과를 A[p..r]에 저장
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:
            k_value = tmp[t]
        i += 1
        t += 1

    


N, K = map(int, input().split())
tmp = [0] * (N + 1)
arr = list(map(int, input().split()))
arr.insert(0, 0)

merge_sort(arr, 1, N)

if cnt < K:
    print(-1)
else:
    print(k_value)