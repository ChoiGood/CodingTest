S = input()

my_set = set()
# 부분 문자열 만들어서 set에 넣기
for i in range(len(S)):
    for j in range(i, len(S)):
        my_set.add(S[i : j + 1])

# print(my_set)
print(len(my_set))