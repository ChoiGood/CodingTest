# 터렛
import math

def solve(r1, r2, d):
    if d < abs(r1 - r2):
        return 0
    
    if d == abs(r1 - r2) or d == r1 + r2:
        return 1

    if d < r1 + r2:
        return 2
    
    if d > r1 + r2:
        return 0

T = int(input())

for tc in range(1, T + 1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.dist((x1, y1), (x2, y2))
    if (x1, y1) == (x2, y2) and r1 == r2:
        print(-1)
    else:
        result = solve(r1, r2, d)
        print(result)