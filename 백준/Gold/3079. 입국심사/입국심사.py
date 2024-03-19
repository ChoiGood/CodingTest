# 입국심사
import sys
input = sys.stdin.readline

def NumberToTime(time):
    cnt = 0
    for t in T:
        if t <= time:
            cnt += time // t
    return cnt

def parameter_search(low, high):
    result = -1
    while low <= high:
        mid = (low + high) // 2
        number = NumberToTime(mid)

        # 1. number가 M(목표 인원) 보다 크다면 => 시간을 줄인다
        if number >= M:
            high = mid - 1
            result = mid
        # 2. number가 M(목표인원) 보다 작다면 => 시간을 키운다
        else: # number < M
            low = mid + 1
    return result

# N : 심사대의 수, M : 사람의 수
N, M = map(int, input().rstrip().split())

# 각 심사대에서 심사를 하는데 걸리는 시간
T = []
for _ in range(N):
    T.append(int(input().rstrip()))

result = parameter_search(0, min(T) * M)
print(result)