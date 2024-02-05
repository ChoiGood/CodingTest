N = int(input())
p_lst = list(map(int, input().split()))
p_lst.sort()

for i in range(1, N):
    p_lst[i] += p_lst[i - 1]

print(sum(p_lst))