# 균형잡힌 세상

while True:
    my_str = input()
    if my_str == '.':
        break
    
    my_stack = []
    flag = True
    for ch in my_str:
        if ch == '(':
            my_stack.append(ch)
        elif ch == '[':
            my_stack.append(ch)
        elif ch == ')': # stack의 top에 ( 이 있는지 확인해주기
            if len(my_stack) == 0:
                flag = False
                break
            if my_stack[-1] == '(':
                my_stack.pop()
            else:
                flag = False
        elif ch == ']': # stack의 top에 [ 이 있는지 확인해주기
            if len(my_stack) == 0:
                flag = False
                break
            if my_stack[-1] == '[':
                my_stack.pop()
            else:
                flag = False
        else:
            pass
    
    if len(my_stack) != 0:
        flag = False
    
    if flag:
        print('yes')
    else:
        print('no')
    
    