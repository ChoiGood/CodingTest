N = int(input())
INF = 9999999
min_count = INF

for i in range(0, 2001):
    for j in range(0, 1001):
        if(3 * i + 5 * j == N):
            if min_count > (i+j) :
                min_count = (i + j)

if min_count != INF :
    print(min_count)
else:
    print(-1)
            