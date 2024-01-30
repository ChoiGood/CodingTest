from collections import deque
# 풍선 터뜨리기
N = int(input())
papers = list(map(int, input().split()))
balloons = list(zip(range(1, N + 1), papers))
#print(balloons)

dq = deque()

dq.extendleft(balloons)

while len(dq) != 1:
    value = dq.pop()
    print(value[0], end = ' ')
    # rotate로 풍선에 적힌 숫자로 움직이기 
    # 회전이 양수일 때는 -1 해줘야한다 <= 원래 있던 수가 pop() 되기 때문
    # 음수일 때는 영향을 끼치지 않는다
    dq.rotate(value[1] - 1 if value[1] > 0 else value[1])
    
print(dq.pop()[0])

