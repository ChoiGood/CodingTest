import sys
input = sys.stdin.readline

N = int(input())
trophys = [int(input()) for _ in range(N)]

h = 0
cnt = 0
for i in range(N):
    if trophys[i] > h:
        cnt += 1
        h = trophys[i]

print(cnt)

h = 0
cnt = 0
for i in range(N - 1, -1, -1):
    if trophys[i] > h:
        cnt += 1
        h = trophys[i]

print(cnt)