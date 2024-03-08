# 부등호
opers = {
    '<' : lambda a, b: a < b,
    '>' : lambda a, b: a > b
}


result = []
def makeNumberArr(d, path):
    if d == N + 1:
        # path 값들을 계산해서 결과 list에 넣어주기
        temp = ''.join(list(map(str, path)))
        result.append(temp)
        return
    
    for i in range(10):
        if not used[i]:
            if d == 0 or (d != 0 and opers[arr[d]](path[-1], i)): 
                used[i] = True
                path.append(i)
                makeNumberArr(d + 1, path)
                path.pop()
                used[i] = False
    


N = int(input())
arr = input().split()
arr.insert(0, -9999)
used = [False] * 10

makeNumberArr(0, [])

result.sort(key = lambda x: int(x))
print(result[-1])
print(result[0])