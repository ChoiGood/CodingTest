# 2. set 사용
N = int(input())
my_set = set(map(int, input().split()))
M = int(input())
search_list = list(map(int, input().split()))
for num in search_list:
    if num in my_set:
        print(1, end = ' ')
    else:
        print(0, end = ' ')