N = int(input())
my_list = list(map(int, input().split()))

my_cards = dict()
for card in my_list:
    if my_cards.get(card) == None:
        my_cards[card] = 1
    else:
        my_cards[card] += 1

M = int(input())
search_list = list(map(int, input().split()))

for num in search_list:
    if my_cards.get(num) == None:
        print(0, end = ' ')
    else:
        print(my_cards[num], end = ' ')