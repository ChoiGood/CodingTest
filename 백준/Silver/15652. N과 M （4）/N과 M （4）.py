def backTrackingEx(n, N, M, arr):
    if n == M:
        print(*arr)
    else:
        tmp = arr[:]
        for i in range(1, N + 1):
            if len(tmp) != 0 and tmp[-1] > i:
                continue
            tmp.append(i)
            backTrackingEx(n + 1, N, M, tmp)
            tmp.pop()

N, M = map(int, input().split())

backTrackingEx(0, N, M, [])