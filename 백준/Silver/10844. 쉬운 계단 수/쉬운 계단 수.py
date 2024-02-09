# 쉬운 계단 수

N = int(input())

dp = [0] * 101
dp[1] = 9

check09 = [0] * 101 # 길이 수 idx 에 따른 마지막 숫자가 0, 9 의 숫자

# 1 ~ 100 글자 길이 수 일 떄 마지막 숫자가 0 과 9 인 숫자를 세아리기 위한 로직
d = {} # 현재 상태의 마지막 숫자들의 상태를 표현하기 위한 딕셔너리
d[0] = 0
for i in range(1, 10):
    d[i] = 1

check09[1] = 1
tmp = [0] * 10
for i in range(2, 101):
    # 딕셔너리를 i 의 상태값으로 바꿔주기
    for j in range(10):
        tmp[j] = d[j]
        d[j] = 0


    for j in range(10):
        if j == 0:
            d[j + 1] += tmp[j]
        elif j == 9:
            d[j - 1] += tmp[j]
        else:
            d[j - 1] += tmp[j]
            d[j + 1] += tmp[j]

    # 딕셔너리의 0 과 9 값을 check 배열에 넣어주기
    check09[i] = d[0] + d[9]

# check 배열 정보를 활용해 dp 테이블 만들기
    
for i in range(2, 101):
    dp[i] = (2 * dp[i - 1] - check09[i - 1]) % 1000000000


print(dp[N])





