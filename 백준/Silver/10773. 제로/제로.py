import sys
# 제로

my_list = []
K = int(input())
for _ in range(K):
    number = int(sys.stdin.readline().rstrip())
    
    if number == 0:
        my_list.pop()
    else:
        my_list.append(number)
        
print(sum(my_list))    