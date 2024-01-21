INF = 0xFFFF

my_list = [[INF] * 15 for _ in range(5)]
#print(my_list)
for i in range(5):
    temp_str = input()
    for j, ch in enumerate(temp_str):
        my_list[i][j] = ch

#print(my_list)

for j in range(15):
    for i in range(5):
        if(my_list[i][j] != INF):
            print(my_list[i][j], end = '')
    
    

