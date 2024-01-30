from collections import deque

N = int(input())

card_list = list(range(1, N + 1))

my_dq = deque()
my_dq.extendleft(card_list)

while len(my_dq) != 1:
    my_dq.pop()
    my_dq.appendleft(my_dq.pop())

print(my_dq.pop())