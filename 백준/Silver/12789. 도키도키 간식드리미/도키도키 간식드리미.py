N = int(input())
line = list(map(int, input().split()))
line.reverse() # line 리스트를 스택처럼 사용하기 위해 역순으로 바꿔줌
# print(line)
side_line = [] # side_line 을 스택으로 구현
num = 1
flag = True
while line :
    if line[-1] == num:
        line.pop()
        num += 1
    elif side_line and side_line[-1] == num:
        side_line.pop()
        num += 1 
    else: # num 이 아니면 side_line 으로 넣어줘야함  --> side_line 에 차곡차곡(side_stack의 top 이 들어오는 수보다 커야함) 
          # 그렇지 못한 경우 false 임!!
        if (not side_line) or (side_line[-1] > line[-1]):
            side_line.append((line.pop()))
        else :
            flag = False
            break

if flag:
    print('Nice')
else :
    print('Sad')