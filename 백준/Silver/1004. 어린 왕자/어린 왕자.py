# 어린 왕자

# 1. 해당 점이 원안에 있는 지 확인해주는 함수
import math
def InCircle(target, c, r): # target, 원의 중심, 반지름 길이
    d = math.dist(target, c)
    return d <= r

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split()) # 출발점, 도착점
    n = int(input()) # 행성계의 개수
    
    cnt = 0
    for _ in range(n):
        c1, c2, r = map(int, input().split())

        flag1 = InCircle((x1,y1), (c1, c2), r)
        flag2 = InCircle((x2, y2), (c1, c2), r)

        if flag1 ^ flag2: # 둘이 다르면 True
            cnt += 1

    print(cnt)