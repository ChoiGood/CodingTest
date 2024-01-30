import sys
N = int(input())
my_set = set()

cnt = 0 # 곰곰티콘
for _ in range(N):
    log = sys.stdin.readline().rstrip()
    
    if log == 'ENTER':
        cnt += len(my_set)
        my_set.clear()
    else:
        if log not in my_set:
            my_set.add(log)
cnt += len(my_set) # 마지막에 Enter끝난다는 보장이 없으므로 반복문이 끝나고 개수 더해주기

print(cnt)
