# 피보나치 수 6
# 피보나치 수의 점근식을 이용해 행렬으로 피보나치 수를 표현한다.
# 행렬의 거듭 제곱을 이용해서 계산한다. => O(2^3 x log n)
MOD = 1000000007
FIBO = [[1, 1], [1, 0]]
def fibo_product(A, B):
    n = len(A)

    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= MOD
    return C

def fibo_sqrt(B):
    if B == 1:
        return FIBO
    
    x = fibo_sqrt(B // 2)
    if B % 2 == 0:
        return fibo_product(x, x)
    else:
        return fibo_product(fibo_product(x, x), FIBO)
    
def solve(N):
    if N == 1:
        print(1)
    else: # N >= 2 인 경우
        result = fibo_sqrt(N - 1)
        print(result[0][0])

N = int(input())
solve(N)
