import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dq = deque()

for _ in range(N):
    tmp = input().rstrip()
    cmd, x = '', 0
    if tmp.isalpha():
        cmd = tmp
    else:
        cmd, x = tmp.split()
        x = int(x)

    if cmd == 'push':
        dq.appendleft(x)
    elif cmd == 'pop':
        if len(dq) != 0:
            value = dq.pop()
            print(value)
        else:
            print(-1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)
    elif cmd == 'back':
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    else:
        print('잘못된 명령')