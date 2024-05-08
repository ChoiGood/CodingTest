
result = {
    0:'E',
    1:'A',
    2:'B',
    3:'C',
    4:'D',
}

while True:
    try:
        arr = list(map(int, input().split()))
        cnt = arr.count(0)
        print(result[cnt])
    except EOFError:
        break