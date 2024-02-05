# 스택
import sys
input = sys.stdin.readline

N = int(input())

my_stack = []
for _ in range(N):
    tmp = input().rstrip()
    cmd, x = '', 0
    if tmp.isalpha():
        cmd = tmp
    else:
        cmd, x = tmp.split()
        x = int(x)

    if cmd == 'push':
        my_stack.append(x)
    elif cmd == 'pop':
        if len(my_stack) != 0:
            value = my_stack.pop()
            print(value)
        else:
            print(-1)
    elif cmd == 'size':
        print(len(my_stack))
    elif cmd == 'empty':
        if len(my_stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(my_stack) != 0:
            print(my_stack[-1])
        else:
            print(-1)
    else:
        print('잘못된 명령')