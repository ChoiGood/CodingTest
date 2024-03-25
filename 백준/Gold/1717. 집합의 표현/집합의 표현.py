# 집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return
    
    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

n, m = map(int, input().split())
parents = list(range(n + 1))
for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union(a, b)
    elif cmd == 1:
        root_a = find_set(a)
        root_b = find_set(b)

        if root_a == root_b:
            print('YES')
        else:
            print('NO')