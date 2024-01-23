while(True):
    n = int(input())
    if(n == -1):
        break
    div_list = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            div_list.append(i)
    
    if(sum(div_list) == n):
        print(n, end = ' = ')
        for i in range(len(div_list)-1):
            print(div_list[i], end = ' + ')
        print(div_list[len(div_list) - 1])
    else:
        print(f'{n} is NOT perfect.')