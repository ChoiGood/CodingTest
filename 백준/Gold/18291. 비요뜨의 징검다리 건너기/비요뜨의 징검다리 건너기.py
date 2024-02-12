# 비요뜨의 징검다리 건더기
def fpow(C, n):
    if n == 1:
        return C
    else:
        x = fpow(C, n // 2) % 1000000007
        if n % 2 == 0:
            return (x * x) % 1000000007
        else:
            return (x * x * C) % 1000000007

def solve(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fpow(2, n - 2)
    
T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
        