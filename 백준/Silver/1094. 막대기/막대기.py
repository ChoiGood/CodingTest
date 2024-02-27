cnt = 0

def stick(my_stick, X):
    global cnt
    if X == 0:
        return
    cnt += 1

    while my_stick > X:
        my_stick //= 2
    stick(my_stick, X - my_stick)

X = int(input())
stick(64, X)

print(cnt)