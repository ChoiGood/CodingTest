white_paper = [[0] * 100 for _ in range(100)]

N = int(input())

#print(list(range(10, 0 , -1)))

for i in range(N):
    s_col, s_row = map(int, input().split())
    for i in range(99 - s_row, 99 - s_row - 10, -1):
        for j in range(s_col, s_col + 10):
            white_paper[i][j] = -1

count = 0
for i in range(100):
    for j in range(100):
        if(white_paper[i][j] == -1):
            count += 1

print(count)

