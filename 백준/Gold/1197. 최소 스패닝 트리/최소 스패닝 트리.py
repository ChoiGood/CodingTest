# 최소 스패닝 트리
# Kruskal 알고리즘 : 모든 Edge 에 대해서 제일 작은 순으로 N -1 개를 뽑는다.
# 간선을 뽑는 와중에 cycle이 생기면 그 간선은 뽑지 않고 다음으로 작은 간선에 대해 검사한다.
import sys
input = sys.stdin.readline

def find_set(x):
    if parents[x] == x:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

V, E = map(int, input().split())
edges = []
parents = list(range(V + 1))

for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))

edges.sort() # 가중치를 기준으로 오름차순 정렬

# V - 1 개의 간선을 선택하면 최소비용 신장트리가 완성
#      : 가장 작은 가중치를 가진 간선을 추가시킴
# 간선을 추가시킬 떄 Cycle이 생성된다면 다음 간선으로 넘어가
weight_sum = 0
cnt = 0

for w, s, e in edges:
    # cycle이 발생하면 pass
    if find_set(s) == find_set(e):
        continue

    # 발생하지 않으면 추가
    union(s, e)
    cnt += 1
    weight_sum += w

    if cnt == V - 1:
        break

print(weight_sum)