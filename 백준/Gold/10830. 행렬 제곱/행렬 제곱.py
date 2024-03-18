# 행렬 제곱
def matrix_product(A, B):
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000
    return C

def matrix_sqrt(arr, B):
    if B == 1:
        return arr

    x = matrix_sqrt(arr, B // 2)
    if B % 2 == 0:
        return matrix_product(x, x)
    else:
        return matrix_product(matrix_product(x, x), arr)

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        arr[i][j] %= 1000

result_arr = matrix_sqrt(arr, B)
for a in result_arr:
    print(*a)