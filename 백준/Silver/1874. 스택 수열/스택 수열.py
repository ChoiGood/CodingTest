import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input().rstrip()))


result = [] # push pop 정보가 담길 배열
flag = True # 수열이 구현 가능함을 판단하는 변수
my_stack = []
i = 1
for num in numbers:
    while i <= num:
        result.append('+')
        my_stack.append(i)
        i += 1

    # i > num 일 때는 my_stack에서 나와야함
    if len(my_stack) != 0 and my_stack[-1] == num:
        result.append('-')
        my_stack.pop()
    else:
        flag = False
        break
    
if flag:
    for a in result:
        print(a)
else:
    print('NO')