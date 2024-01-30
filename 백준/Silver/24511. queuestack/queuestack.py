from collections import deque

qstack = deque()
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 문제를 잘 읽고 분석하면 queuestack이 
# 결국 queue 인 자료구조들의 값들을 넣어서 하나의 큐로 연결하면 구현이 가능함

# qstack 만들기
for idx, value in enumerate(A):
    if value == 0:
        qstack.append(B[idx])


M = int(input())
C = list(map(int, input().split()))

for num in C:
    qstack.appendleft(num)
    print(qstack.pop(), end = ' ')