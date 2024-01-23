a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if(a1 > c):
    print(0)
else: # 이 부분 삼항 연산자로 구현하기
    if a1 == c :
        if a0 <= 0 :
            print(1)
        else:
            print(0)
    else : # a1 < c
        x = a0 / (c - a1)
        if(n0 >= x):
            print(1)
        else:
            print(0)