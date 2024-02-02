import copy
def check(arr, value, row, col):
    if value in arr[row]:
        return False

    for i in range(9):
        if i != row and arr[i][col] == value:
            return False

    s_row = row // 3
    s_col = col // 3

    for i in range(3 * s_row, 3 * s_row + 3):   # i : 3 * s_row -> 3 * s_row + 2
        for j in range(3 * s_col, 3 * s_col + 3):
            if i == row and j == col:
                continue
            if arr[i][j] == value:
                return False
    return True
cnt = 0
def solveSdocu(t_len, d, t_list, arr):
    global cnt
    if cnt >= 1:
        return
    if d == t_len:
        cnt += 1
        for row in arr:
            print(*row)
    else:
        row, col = t_list[d]
        for value in range(1, 10):
            if check(arr, value, row, col):
                arr[row][col] = value
                solveSdocu(t_len, d + 1, t_list, arr)
                arr[row][col] = 0


arr = [list(map(int, input().split())) for _ in range(9)]
t_list = [] # 빈 칸의 위치를 표현해주는 tuple 들의 리스트 만들기
# S = copy.deepcopy(arr)

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            t_list.append((i, j))
# print(len(t_list))
solveSdocu(len(t_list), 0, t_list, arr)