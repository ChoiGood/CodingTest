# # 스택 2
# # 리스트의 append() 와 pop으로 stack 처럼 활용
import sys

def empty(my_stack):
    if len(my_stack) == 0:
        return True
    else:
        return False

my_stack = []
N = int(input())
for _ in range(N):
    command = -1
    temp = sys.stdin.readline().rstrip()
    try :
        command = int(temp)
    except ValueError:
        command, X = map(int, temp.split())
        
    if command == 1:
        my_stack.append(X)
    elif command == 2:
        if empty(my_stack):
            print(-1)
        else:
            print(my_stack.pop())
    elif command == 3:
        print(len(my_stack))
    elif command == 4:
        if empty(my_stack):
            print(1)
        else:
            print(0)
    elif command == 5:
        if empty(my_stack):
            print(-1)
        else:
            print(my_stack[-1])
    else:
        print('잘못된 명령어를 입력했습니다.')

