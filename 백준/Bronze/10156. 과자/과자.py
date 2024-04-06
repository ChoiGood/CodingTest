K, N, M = map(int, input().split())

print(0 if K*N - M < 0 else K*N - M)