my_list = []

for _ in range(5):
    num = int(input())
    my_list.append(num)
    
my_list.sort()
print(sum(my_list) // 5)
print(my_list[2])