
def promising(result, value):
    if len(result) == 0:
        return True
    n = len(result)
    for i in range(1, n // 2 + 1):
        if result[-i:] == result[-2*i:-i]:
            return False
    return True


mn_value = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
def dfs(result, s):
    global mn_value
    if len(result) == N:
        if mn_value > s:
            mn_value = s
        return
    if s > mn_value:
        return
    for value in [1, 2, 3]:
        result.append(value)
        if promising(result, value):
            dfs(result, s + value * 10 ** (N - len(result)))
        result.pop()

N = int(input())
dfs([], 0)

print(mn_value)
