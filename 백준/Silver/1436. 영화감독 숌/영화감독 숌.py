N = int(input())

my_list = []
for i in range(666, 5000000):
    if str(i).find('666') != -1:
        my_list.append(i)
        
#print(len(my_list))
my_list.sort()
print(my_list[N - 1])