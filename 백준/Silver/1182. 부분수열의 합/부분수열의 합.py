# 부분수열의 합
cnt = 0
def dfs(d, lst):
    global cnt
    if d == N: # 기저 조건
        if sum(lst) == S and lst: # 크기가 양수이고 합이 S인 부분 수열
            cnt += 1
        return

    # 인덱스 d를 포함
    dfs(d + 1, lst + [arr[d]])

    # 인덱스 d를 포함 x
    dfs(d + 1, lst) 




N, S = map(int, input().split())
visited = [0] * N
arr = list(map(int, input().split()))

dfs(0, [])
print(cnt)