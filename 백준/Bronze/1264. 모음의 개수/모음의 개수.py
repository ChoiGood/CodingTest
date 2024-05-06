while True:
    s = input().lower()

    if s == '#':
        break
    
    cnt = 0

    for ch in s:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1

    print(cnt)

