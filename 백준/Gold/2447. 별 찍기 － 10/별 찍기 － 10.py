def star(N, r, c, arr):
    if N == 3: # 종료조건
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                arr[r + i][c + j] = '*'
    else:
        for i in range(r, r + N, N // 3):
            for j in range(c, c + N, N // 3):
                if (i == (r + N // 3)) and (j == (c + N // 3)):
                    continue
                star(N//3, i, j, arr)
    

N = int(input())
arr = [[' '] * (N + 1) for _ in range(N + 1)]

star(N, 1, 1, arr)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(arr[i][j], end = '')
    print()