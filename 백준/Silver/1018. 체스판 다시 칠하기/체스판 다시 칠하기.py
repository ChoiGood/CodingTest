def chess_count(my_list, row, col):
    #예쁘게 어케 짬?
    # 왼쪽 위가 W 일 경우
    count1 = 0
    for i in range(8):
        check1 = 'W' if i % 2 == 0 else 'B'
        check2 = 'B' if i % 2 == 0 else 'W'
        
        for j in range(8):
            if j % 2 == 0 :
                if my_list[row + i][col + j] != check1:
                    count1 += 1
            else :
                if my_list[row + i][col + j] != check2:
                    count1 += 1

    # 왼쪽 위가 B 일 경우
    count2 = 0
    for i in range(8):
        check1 = 'W' if i % 2 == 1 else 'B'
        check2 = 'B' if i % 2 == 1 else 'W'
        
        for j in range(8):
            if j % 2 == 0 :
                if my_list[row + i][col + j] != check1:
                    count2 += 1
            else :
                if my_list[row + i][col + j] != check2:
                    count2 += 1
                    
    if count1 > count2 :
        return count2
    else:
        return count1




N, M = map(int, input().split())

my_list = [list(input()) for _ in range(N)]

min_count = 99999
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        count = chess_count(my_list, i , j)
        if(count < min_count) :
            min_count = count
            
print(min_count)
