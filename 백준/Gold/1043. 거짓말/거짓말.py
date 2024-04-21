# 거짓말

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return
    
    parent[root_y] = root_x


N, M = map(int, input().split()) # 사람의 수 N, 파티의 수 M
parent = list(range(N + 1))

know, *knownPerson = list(map(int, input().split()))

parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

if know == 0:
    print(M)
else:
    rep = knownPerson[0]
    # 진실을 아는 사람들 union
    for person in knownPerson:
        union(rep, person)

    # party를 돌면서도 union 시키기
    for party in parties:
        party_rep = party[0]
        for person in party:
            union(party_rep, person)

    # 다시 한번 파티를 돌면서 fake 수 구하기
    fake_cnt = 0

    for party in parties:
        is_fake = True  # 해당 파티에 사기 칠 수 있는 여부 판단

        # 현재 파티 안의 사람들 중 진실을 아는 집합에 있는 사람들이 모두 없니면
        for person in party:
            if find(rep) == find(person):
                is_fake = False
                break

        if is_fake:
            fake_cnt += 1    
    print(fake_cnt)