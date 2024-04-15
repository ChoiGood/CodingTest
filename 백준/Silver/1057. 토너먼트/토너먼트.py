# 토너먼트
def play(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number // 2 + 1

N, a, b = map(int, input().split())
cnt = 0
while True:
    a, b = play(a), play(b)
    cnt += 1

    if a == b:
        break

print(cnt)
