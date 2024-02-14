from collections import deque

def max_t(t):
    tmp_max = -999
    for value, idx in t:
        if tmp_max < value:
            tmp_max = value
    return tmp_max


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = []
    dq = deque()

    for i in range(N):
        dq.appendleft((arr[i], i))

    while len(dq) != 0:
        if dq[-1][0] == max_t(dq):
            result.append(dq.pop())
        else:
            dq.appendleft(dq.pop())

    for i in range(N):
        if result[i][1] == M:
            print(i + 1)
