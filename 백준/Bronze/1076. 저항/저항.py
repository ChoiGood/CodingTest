c_lst = ['black', 'brown', 'red', 'orange',
         'yellow', 'green', 'blue', 'violet',
         'grey', 'white']
color_value_mul = {}

for idx, color in enumerate(c_lst):
    color_value_mul[color] = (idx, 10**idx)

c_first = input()
c_second = input()
c_third = input()

print((color_value_mul[c_first][0] * 10 + color_value_mul[c_second][0]) * color_value_mul[c_third][1])

