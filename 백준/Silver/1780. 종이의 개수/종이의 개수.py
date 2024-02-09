result = [0] * 3 # 0 1 -1 개수

def check(N, row, col, arr):
    value = arr[row][col]
    for i in range(N):
        for j in range(N):
            if arr[row + i][col + j] != value:
                return False
    return True

def paper(N, row, col, arr):
    if check(N, row, col, arr): # 종료 조건
        global result
        value = arr[row][col]
        result[value] += 1
    else:                   # 재귀 조건
        for i in range(row, row + N, N//3):
            for j in range(col, col + N, N // 3):
                paper(N//3, i, j, arr)
    
N = int(input()) # 3**k 꼴로 주어진다
arr = [list(map(int, input().split())) for _ in range(N)]

paper(N, 0, 0, arr)

print(result[-1])
print(result[0])
print(result[1])
