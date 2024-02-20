# import sys
# input = sys.stdin.readline

def dfs(d, idx, lotto):
    if d == 6:
        print(*lotto)
    else:
        for i in range(idx, k):
            lotto.append(arr[i])
            dfs(d + 1, i + 1, lotto)
            lotto.pop()

while True:
    tmp = input().rstrip()
    if tmp == '0':
        break
    
    arr = list(map(int, tmp.split()))
    k = arr[0]
    arr = arr[1:]

    dfs(0, 0, [])
    print()