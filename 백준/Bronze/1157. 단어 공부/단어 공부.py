my_string = input().lower()

my_list = list(my_string)

my_dict = {}

for i in range(len(my_string)):
    if my_dict.get(my_list[i]) == None:
        my_dict[my_list[i]] = 1
    else:
        my_dict[my_list[i]] += 1


my_sorted_dict = sorted(my_dict.items(), key = lambda x : x[1], reverse = True)



if(len(my_sorted_dict) != 1):
    if(my_sorted_dict[0][1] == my_sorted_dict[1][1]):
        print('?')
    else:
        print(str(my_sorted_dict[0][0]).upper())
else :
    print(str(my_sorted_dict[0][0]).upper())


