# 단지번호붙이기
d_row = [0, 0, 1, -1] # 우 좌 하 상
d_col = [1, -1, 0, 0]

cnt = 0
def findHome(row, col, arr): 
    '''
    dfs 탐색하면서 cnt 계산해주는 함수
    arr 에 체크한 집은 -1로 변경
    '''
    global cnt
    if arr[row][col] != 1: # 기저 조건
        return
    else: # 재귀 조건
        arr[row][col] = -1 # 방문 처리
        cnt += 1
        
        for d in range(4):
            n_r = row + d_row[d]
            n_c = col + d_col[d]

            if 0 <= n_r < n and 0 <= n_c < n:
                findHome(n_r, n_c, arr)

# 입력
n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]

# 로직
t_cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            t_cnt += 1
            cnt = 0
            findHome(i, j, arr)
            result.append(cnt)

# 출력
print(t_cnt)
result.sort() # 단지 수는 오름차순 정렬 후 하나씩 출력
for num in result:
    print(num)
            


