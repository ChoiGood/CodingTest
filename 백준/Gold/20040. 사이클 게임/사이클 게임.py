import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union_by_rank(x, y):
    root_x = find(x)
    root_y = find(y)

    # 같은 집합이면 True를 반환 => 싸이클이 생성됨
    if root_x == root_y:
        return True

    # union by rank
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else: # rank 가 같은 경우 임의로 붙이기
        parent[root_y] = root_x
        rank[root_x] += 1

    return False

n, m = map(int, input().split())
parent = list(range(n))
rank = [0] * n

result = float('inf')
for round in range(1, m + 1):
    x, y = map(int, input().split())

    if union_by_rank(x, y):
        result = min(result, round)

print(0 if result == float('inf') else result)