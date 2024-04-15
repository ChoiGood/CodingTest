# 친구 네트워크
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    
    # 경로 압축
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    # 대표자를 구하기
    root_x = find(x)
    root_y = find(y)

    # x, y 가 같은 집합인 경우
    if root_x == root_y:
        print(t_size[root_x])
        return
    
    # x, y 가 다른 집합인 경우
    # 사이즈가 큰 녀석에 사이즈가 작은 녀석을 붙인다.
    
    # 항상 root_x 가 크게 만들기
    if t_size[root_x] < t_size[root_y]:
        root_x, root_y = root_y, root_x  # swap

    # union
    parent[root_y] = root_x
    t_size[root_x] += t_size[root_y]
    
    print(t_size[root_x])


T = int(input()) # 테스트 케이스 수

for _ in range(T):
    F = int(input())

    name_to_id = {} # 이름과 매칭 되는 id , 이 id를 union-find에 사용된다.
    friends = [] # 친구 관계를 저장할 배열

    n = 0 # 총 인원 수
    for _ in range(F):
        person1, person2 = input().split()

        for person in [person1, person2]:
            if name_to_id.get(person) == None:
                n += 1
                name_to_id[person] = n

        friends.append((person1, person2))
    
    parent = [i for i in range(n + 1)]
    t_size = [1] * (n + 1)

    for person1, person2 in friends:
        p1 = name_to_id[person1]
        p2 = name_to_id[person2]

        union(p1, p2)