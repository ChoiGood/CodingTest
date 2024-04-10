# 수열의 합

N, L = map(int, input().split())

result = -1

for l in range(L, 100 + 1):
    a = int(((2 * N / l) - (l - 1)) / 2)

    if a < 0:
        result = -1
        break

    if (2*a + l - 1) * l == 2*N:
        result = (a, l)
        break

if result == -1:
    print(-1)
else:
    print(*range(result[0], result[0] + result[1]))