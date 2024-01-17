N = int(input())

# 흠 간추리는 방법을 모르겠는데?

for i in range(1, N):
    print(' ' * (N - i), end = '')
    print('*' * (2*i-1))

print('*' * (2*N - 1))


temp = list(range(1,N))
temp = temp[::-1]

for i in temp:
    print(' ' * (N - i), end = '')
    print('*' * (2*i-1))
