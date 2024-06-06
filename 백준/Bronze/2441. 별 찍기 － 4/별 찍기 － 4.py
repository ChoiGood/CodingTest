N = int(input())   
sum = 0                     # 공백 출력 변수

for i in range(N, 0, -1) :  # 거꾸 감소하는 반복문
    for k in range(sum) :   # 공백의 개수 증가하며 출력력
        print(' ', end = "")
    for j in range(i) :
        print('*', end = "")
    sum += 1
    print('') 