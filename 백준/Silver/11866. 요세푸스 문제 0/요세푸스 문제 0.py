# 요세푸스 문제 0
from collections import deque

N, K = map(int, input().split())

result_list = []
osepus_dq = deque()
osepus_dq.extendleft((range(1, N + 1)))

while len(osepus_dq) != 1: # 사람이 한명 남을 때 까지 지속
    # K번째 사람을 죽이자
    for _ in range(1, K): # 1 ~ k - 1 번 째 사람들은 보내기
        osepus_dq.appendleft(osepus_dq.pop())
    result_list.append(osepus_dq.pop()) # k번쨰 사람 죽이기
    
result_list.append(osepus_dq.pop())

print('<', end = '')
print(*result_list, sep = ', ', end = '')
print('>')
    

