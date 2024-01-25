import sys


N = int(sys.stdin.readline().rstrip())

my_list = []
for i in range(N):
    my_list.append(int(sys.stdin.readline().rstrip()))

my_list.sort()

for i in range(N):
    print(my_list[i])