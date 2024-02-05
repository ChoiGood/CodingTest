# 보물
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

t_sum = 0
for i in range(N):
    t_sum += A[i] * B[i]

print(t_sum)