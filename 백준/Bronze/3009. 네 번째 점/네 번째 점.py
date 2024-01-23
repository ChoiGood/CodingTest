dict_x = {}
dict_y = {}

for _ in range(3):
    x, y = map(int, input().split())
    if(dict_x.get(x) == None):
        dict_x[x] = 1
    else:
        dict_x[x] += 1
        
    if(dict_y.get(y) == None):
        dict_y[y] = 1
    else:
        dict_y[y] += 1
        
for key, item in dict_x.items():
    if(item != 2):
        print(key, end = ' ')
        
for key, item in dict_y.items():
    if(item != 2):
        print(key)
    