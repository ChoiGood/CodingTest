def backtrackEx(len, N, M, arr):
    if len == M:
        print(*arr)
    else:
        tmp = arr[:] # 배열 복사해주기 (깊은 복사)
        for i in range(1, N + 1):
            tmp.append(i)
            backtrackEx(len + 1, N, M, tmp)
            tmp.pop()

N, M = map(int, input().split())
backtrackEx(0, N, M, [])