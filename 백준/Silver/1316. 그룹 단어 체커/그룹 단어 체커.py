def check(my_string):
    """그룹 단어가 아닌지 맞는 지 판단해줌

    Args:
        check (str): 그룹 단어가 아닌지 맞는 지 판단해줌
    """
    my_memory = []
    i = 0
    # aaaaaa
    while True:
        #print(i, my_memory)
        # my_memory 에 있는 지 확인하기
        if my_string[i] not in my_memory: # 없다면 연속된 값들 쭈욱 넣기
            my_memory.append(my_string[i])
            # 다른 문자 나타날때 까지 index 이동
            while(i < (len(my_string) - 1) and my_string[i] == my_string[i+1]):
                i += 1
            i += 1 # 다른 문자로 이동해서 다음꺼 판단해보자
            
        else : # 있다면 이 단어는 그룹 단어가 아니군!!
            return False
        
        if i >= (len(my_string)):
            break
        
    return True

answer = 0
N = int(input())
for _ in range(N):
    my_string = input()
    if(check(my_string)):
        answer += 1
    
print(answer)