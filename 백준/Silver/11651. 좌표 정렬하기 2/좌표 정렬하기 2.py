N = int(input())
my_list = []
for _ in range(N):
    temp = tuple(map(int, input().split()))
    my_list.append(temp)

#my_list.sort()
my_list.sort(key=lambda x : (x[1], x[0])) # 자동으로 (요소의 오름차순) 파이썬에서 해주는데 이걸 내가 설정할려면??

for i in range(N):
    print(f'{my_list[i][0]} {my_list[i][1]}')
