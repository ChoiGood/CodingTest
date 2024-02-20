# 1, 2, 3 더하기
cnt = 0
def oneTwoThree(value):
    global cnt
    if value == N: # 기저 조건
        cnt += 1
        return
    elif value > N:
        return
    else:
        for i in range(1, 4):
            oneTwoThree(value + i)
    # oneTwoThree(value + 1)
    # oneTwoThree(value + 2)
    # oneTwoThree(value + 3)

T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    oneTwoThree(0)
    print(cnt)