# 명령 프롬프트
import sys
input = sys.stdin.readline

N = int(input()) # 파일 이름의 개수 N
files = [input() for _ in range(N)]

l = len(files[0])

result = []
for i in range(l):
    temp = set()
    for file in files:
        temp.add(file[i])
    if len(temp) == 1:
        result.append(files[0][i])
    else:
        result.append('?')

print(''.join(result))