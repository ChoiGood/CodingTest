import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    tmp_sum = 0
    for _ in range(N):
        number = int(input())
        tmp_sum += number

    answer = 0 if tmp_sum == 0 else ('+' if tmp_sum > 0 else '-')
    print(answer)