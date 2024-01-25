# 단어 정렬
import sys

N = int(sys.stdin.readline().rstrip())

my_list = []

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    my_list.append(temp)

# set 으로 중복을 없애고 sorted로 정렬 시킨다
sorted_list = sorted(set(my_list), key = lambda x : (len(x), x)) 

for word in sorted_list:
    print(word)