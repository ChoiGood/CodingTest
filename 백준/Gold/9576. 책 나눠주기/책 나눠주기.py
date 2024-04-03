# 책 나눠주기
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    book_shared = [False] * (N + 1)
    
    persons = []
    for _ in range(M):
        a, b = map(int, input().split())
        persons.append((a, b))
    persons.sort(key=lambda x : (x[1], x[0]))

    cnt = 0
    for a, b in persons:
        for i in range(a, b + 1):
            if not book_shared[i]:
                book_shared[i] = True
                cnt += 1
                break
    
    print(cnt)
