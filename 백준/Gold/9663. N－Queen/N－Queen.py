# N-Queen
cnt = 0
def n_Queens(n, N, queens): # 깊이, N, 퀸의 리스트(index는 행을 의미, value는 열을 의미)
    if n == N:
        global cnt
        cnt += 1
    else:
        # 퀸 리스트에 담기면 행이 다르다!!
        for c_col in range(N):
            if c_col not in queens: # values 값이 다름 => 열이 다름을 의미
                c_row = n # 현재 내가 넣는 퀸의 행
                # 이제 대각선에 있지 않음을 확인 해야함!!
                flag = False # 대각선에 있지 않음
                for row, col in enumerate(queens):
                    if abs(row - c_row) == abs(col - c_col):
                        flag = True
                        break
                if flag:
                    continue
                queens.append(c_col)
                n_Queens(n + 1, N, queens)
                queens.pop()


N = int(input())
n_Queens(0, N, [])
print(cnt)