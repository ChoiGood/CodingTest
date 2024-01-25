N = int(input())
my_list = []

for i in range(N):
    temp = int(input())
    my_list.append(temp)

my_list.sort()

for i in range(N):
    print(my_list[i])