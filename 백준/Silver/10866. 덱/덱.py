# 덱
from collections import deque
import sys
input = sys.stdin.readline

#
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

N = int(input().rstrip())

dq = deque()

for _ in range(N):
    try:
        tmp = input().rstrip()
        cmd, x = tmp.split()
    except ValueError:
        cmd = tmp

    if cmd == 'push_front':
        dq.appendleft(x)
    elif cmd == 'push_back':
        dq.append(x)
    elif cmd == 'pop_front':
        print(dq.popleft() if len(dq) != 0 else -1)
    elif cmd == 'pop_back':
        print(dq.pop() if len(dq) != 0 else -1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        print(int(len(dq) == 0))
    elif cmd == 'front':
        print(dq[0] if len(dq) != 0 else -1)
    elif cmd == 'back':
        print(dq[-1] if len(dq) != 0 else -1)
    else:
        print('잘못된 명령입니다.')



