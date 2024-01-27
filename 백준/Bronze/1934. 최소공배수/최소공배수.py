def lcm(n1, n2):
    max_n = max(n1, n2)
    min_n = min(n1, n2)

    i = 1
    while True:
        if(max_n * i) % min_n == 0:
            break
        i += 1
    return max_n * i


T = int(input())
for _ in range(T):
    n1, n2 = map(int, input().split())
    print(lcm(n1,n2))