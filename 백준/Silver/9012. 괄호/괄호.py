# 괄호
T = int(input())

for _ in range(T):
    VPS = input()
    
    flag = True
    my_stack = []
    for bracket in VPS: 
        if bracket == '(':
            my_stack.append(bracket)
        elif bracket == ')':
            if len(my_stack) == 0: # 빈 스텍이면 False
                flag = False
                break
            if my_stack[-1] == '(': # 스택 맨위에 '(' 이 있으면 pop()
                my_stack.pop()
            # else: # 이 부분은 사실 필요가 없군
            #     flag = False
            #     break
        else:
            print('입력된 문자열이 괄호 문자열(VPS)가 아닙니다.')
    
    if len(my_stack) != 0:
        flag = False
    
    if flag:
        print('YES')
    else:
        print('NO')