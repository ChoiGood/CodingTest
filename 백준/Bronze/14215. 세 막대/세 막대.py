# 각 막대의 길이를 마음대로 줄일 수 있다.
# 각 막대의 길이는 양의 정수
# 세 막대를 이용해 넓이가 양수인 삼각형을 만들 수 있어야함
# 둘레를 최대로!!

my_list = list(map(int, input().split()))

max_v = max(my_list)
sum_2e = sum(my_list) - max_v

while True:
    if(max_v < sum_2e):
        break
    max_v -= 1

print(max_v + sum_2e)