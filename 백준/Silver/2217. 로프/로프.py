# 로프
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    number = int(input().rstrip())
    arr.append(number)
arr.sort()

for i in range(N):
    arr[i] = arr[i] * (N - i)

print(max(arr))