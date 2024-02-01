# 인간-컴퓨터 상호작용
# 입력
word = input() # 입력 받은 문자열
T = int(input()) # 질문의 개수

# 로직 (처리)
# 딕셔너리에 각 문자에 대한 누적합을 관리시키자!!
N = len(word) # 문자열의 길이
alpabet_lower = 'abcdefghijklmnopqrstuvwxyz'
d = {}

for alpa in alpabet_lower:
    tmp = [0] * N
    for i, c in enumerate(word):
        if c == alpa:
            tmp[i] += 1
    for i in range(1, N):
        tmp[i] += tmp[i - 1]
    d[alpa] = tmp

for _ in range(T):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    tmp = d[a] # 해당 알파벳에 대한 누적합에 접근

    if l == 0:
        print(tmp[r] - 0)
    else:
        print(tmp[r] - tmp[l - 1])