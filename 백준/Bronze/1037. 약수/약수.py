N = int(input())
div_list = list(map(int, input().split()))

div_list.sort()

if N == 1:
    print(div_list[0] ** 2)
else:
    print(div_list[0] * div_list[-1])
    