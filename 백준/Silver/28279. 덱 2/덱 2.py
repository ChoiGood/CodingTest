# 덱 2
from collections import deque
import sys

N = int(input())

dq = deque()

for _ in range(N):
    cmd, x = -1, -1
    temp = sys.stdin.readline().rstrip()
    if temp.isdigit():
        cmd = int(temp)
    else:
        cmd, x = map(int, temp.split())
    
    if cmd == 1:
        dq.append(x)
    elif cmd == 2:
        dq.appendleft(x)
    elif cmd == 3:
        if len(dq) != 0:
            value = dq.pop()
            print(value)
        else:
            print(-1)
    elif cmd == 4:
        if len(dq) != 0:
            value = dq.popleft()
            print(value)
        else:
            print(-1)
    elif cmd == 5:
        print(len(dq))
    elif cmd == 6:
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 7:
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)
    elif cmd == 8:
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    else :
        print('잘못된 명령')
