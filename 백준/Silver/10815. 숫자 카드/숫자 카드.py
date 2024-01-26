# 숫자카드
N = int(input())
my_list = list(map(int, input().split()))
my_card_set = dict().fromkeys(my_list, 1)

M = int(input())
check_list = list(map(int, input().split()))
for check in check_list:
    if my_card_set.get(check) != None:
        print(1, end = ' ')
    else :
        print(0, end = ' ')