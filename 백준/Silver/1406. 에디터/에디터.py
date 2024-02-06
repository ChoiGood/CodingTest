# # 에디터
from collections import deque
import sys
input = sys.stdin.readline

s1 = input().rstrip()
N = int(input().rstrip())

left = deque()
right = deque()

left.extend(s1)

for _ in range(N):
    tmp = input().rstrip()
    cmd, ch = '', ''
    if tmp.isalpha():
        cmd = tmp
    else:
        cmd, ch = tmp.split()

    if cmd == 'L':
        if len(left) != 0:
            value = left.pop()
            right.appendleft(value)
    elif cmd == 'D':
        if len(right) != 0:
            value = right.popleft()
            left.append(value)
    elif cmd == 'B':
        if len(left) != 0:
            left.pop()
    elif cmd == 'P':
        left.append(ch)
    else:
        print('잘못된 명령')

print(''.join(left), ''.join(right), sep = '')
