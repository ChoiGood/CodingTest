def diffCount(A, B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    return cnt

A, B = input().split()

mn_diff = 100
for i in range(len(B) - len(A) + 1):
    mn_diff = min(mn_diff, diffCount(A, B[i:i + len(A)]))

print(mn_diff)