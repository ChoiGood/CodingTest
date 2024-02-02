max = -1000000000000
min = 1000000000000

def operInsert(N, d, oper_list, opers_num, numbers):
    '''
    :param N: 숫자의 개수
    :param d: dfs 깊이
    :param oper_list: 연산자 리스트 (0 : +, 1 : -, 2 : x, 3 : //)
    :param opers_num: 연산자 개수
    :param numbers: 숫자 리스트 (마지막에 계산 할 때 사용)
    :return: 다 내려가면 max min 최신화
    '''
    if d == N - 1: # 깊이 다 내려옴 계산 해주고 min max 최신화 시키자
        global max
        global min
        # oper_list 와 numbers로 계산해주기
        value = numbers[0]
        for i in range(1, N):
            op = oper_list[i - 1]
            if op == 0:
                value += numbers[i]
            elif op == 1:
                value -= numbers[i]
            elif op == 2:
                value *= numbers[i]
            elif op == 3:
                if value >= 0:
                    value //= numbers[i]
                else:
                    value = - (abs(value) // numbers[i])
        if max < value:
            max = value
        if min > value:
            min = value
    else:
        for idx, value in enumerate(opers_num):
            if value != 0: # 연산자를 넣을 수 있는 상태 (개수가 0 이 아니다)
                oper_list.append(idx)
                opers_num[idx] -= 1
                operInsert(N, d + 1, oper_list, opers_num, numbers)
                oper_list.pop()
                opers_num[idx] += 1


N = int(input())
numbers = list(map(int, input().split()))
opers_num = list(map(int, input().split()))

operInsert(N, 0, [], opers_num, numbers)

print(max)
print(min)
