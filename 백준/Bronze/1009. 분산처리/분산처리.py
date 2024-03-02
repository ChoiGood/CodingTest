import math
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    value = pow(a, b, 10)

    print(value if value != 0 else 10)