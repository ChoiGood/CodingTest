croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

my_string = input()

my_index = 0
answer = 0

def moveindex(search, search_string):
    moving = 1
    for i in range(len(search)):
        if (search_string.find(search[i]) != -1) :
            if(moving < len(search[i])):
                moving = len(search[i])
    return moving
            
# 입력받은 단어를 원 포인터로 돌면서 관련된 알파벳이 있는지 판단하기!!
while(True):
    if my_index > (len(my_string) - 1) :
        break
    search_string = my_string[my_index:my_index + 3]
    my_index += moveindex(croatia, search_string)
    answer += 1

print(answer)
