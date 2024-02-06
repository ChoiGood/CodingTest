from collections import deque

N, K = map(int, input().split())
dq = deque()
dq.extendleft(range(1, N + 1))

result = []

while len(dq) != 1: # 한 사람만 남을 때 까지
    for _ in range(K - 1): # K - 1 번 넘어가
        value = dq.pop()
        dq.appendleft(value)
    result.append(dq.pop()) # K 번쨰 사람 죽이기

result.append(dq.pop()) # 마지막 남은 한 사람 넣어주기
print('<', end = '')
print(*result, sep = ', ', end = '')
print('>')

