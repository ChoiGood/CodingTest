# 주유소
N = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

c_mincst = costs[0]
total = 0
for i in range(N - 1):
    if c_mincst > costs[i]:
        c_mincst = costs[i]
    total += c_mincst * dists[i]
print(total)


# min_idx 전 까지는 해당 거리 최소 단위로 기름 구매
# min_idx 드가면 나머지 거리값 싹다 구매



