from collections import deque
import sys

# appendleft 와 pop 으로 queue 로 사용
my_dq = deque()

N = int(input())

for _ in range(N):
    num = -1
    cmd = sys.stdin.readline().rstrip()
    if(not cmd.isalpha()):
        cmd, num = cmd.split()
        num = int(num)
    
    if cmd == 'push':
        my_dq.appendleft(num)
    elif cmd == 'pop':
        if len(my_dq) != 0:
            value = my_dq.pop()
            print(value)
        else:
            print(-1)
    elif cmd == 'size':
        print(len(my_dq))
    elif cmd == 'empty':
        if len(my_dq) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(my_dq) != 0:
            print(my_dq[-1])
        else:
            print(-1)
    elif cmd == 'back':
        if len(my_dq) != 0:
            print(my_dq[0])
        else:
            print(-1)
    else:
        print('잘못된 명령')
        