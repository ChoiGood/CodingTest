import sys
N = int(sys.stdin.readline().rstrip())

# 메모리를 제한함!! 일반적인 sort 쓰기위해
# list 를 길게 만들면 N 10,000,000 이기 때문에
# 메모리 초과가 발생한다

# 문제의 조건에서 수가 10,000 보다 작거나 같은 자연수이기 때문에!!
# 이를 활용하여 문제를 해결하자!!

my_list = [0] * 10001

for _ in range(N):
    temp = int(sys.stdin.readline().rstrip())
    my_list[temp] += 1

for i in range(1, 10001):
    for _ in range(my_list[i]):
        print(i)