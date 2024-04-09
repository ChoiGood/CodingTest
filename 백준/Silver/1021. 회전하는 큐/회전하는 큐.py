# 회전하는 큐
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
dq.extend(list(range(1, N + 1)))

cnt = 0

for a in arr:
    if dq[0] == a:
        dq.popleft()
    else:
        tmp_cnt = 0
        while dq[0] != a:
            tmp_cnt += 1
            dq.append(dq.popleft())
        cnt += min(tmp_cnt, len(dq)-tmp_cnt)
        dq.popleft()

print(cnt)