N, K = map(int, input().split())

div_list = []

for i in range(1, N + 1):
    if (N % i == 0):
        div_list.append(i)

if(len(div_list) < K):
    print(0)
else:
    print(div_list[K-1])