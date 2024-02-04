import sys
input = sys.stdin.readline

N = int(input())

confers = []
for _ in range(N):
    confers.append(tuple(map(int, input().split())))

confers.sort(key = lambda x : (x[1], x[0]))

cnt = 0
t_e = -1
for confer in confers:
    s, e = confer
    if e >= t_e and s >= t_e:
        cnt += 1
        t_e = e

print(cnt)



