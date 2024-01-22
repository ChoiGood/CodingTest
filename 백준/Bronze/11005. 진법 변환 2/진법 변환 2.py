# 진법 변환
number_10, base = map(int, input().split())

# ord('A') = 65
# print(ord('A') - 55)
my_dict = {}
for i in range(0, 10):
    my_dict[i] = str(i)
my_temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for char in my_temp:
    my_dict[ord(char) - 55] = char

#print(my_dict)

result = []
while(number_10 > 0):
    temp = number_10 % base
    result.append(my_dict[temp])
    number_10 //= base

result.reverse()
print(''.join(result))


