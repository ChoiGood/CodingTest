# 영단어 암기는 괴로워
# 딕셔너리 카운트
import sys

N, M = map(int, input().split())
dct = {}
for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    if len(temp) < M:
        continue
    if dct.get(temp) == None:
        dct[temp] = 1
    else:
        dct[temp] += 1

result_list = sorted(dct.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for ch in result_list:
    print(ch[0])

