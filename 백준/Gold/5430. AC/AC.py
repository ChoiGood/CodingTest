# AC

from collections import deque
import re

T = int(input())

for _ in range(T):
    fuc = input()
    n = int(input())
    tmp = input()
    arr = re.findall(r'\d+', tmp)

    dq = deque()
    dq.extend(arr)
    r_flag = False
    e_flag = False
    for ch in fuc:
        if ch == 'R':
            r_flag = not r_flag
        elif ch == 'D':
            if len(dq) == 0:
                e_flag = True
            else:
                dq.pop() if r_flag else dq.popleft()
        else:
            print('잘못된 명령')
    
    if e_flag:
        print('error')
    else:
        if r_flag:
            dq.reverse()
        print('[', end = '')
        
        print(*dq, sep = ',', end = ']\n')

