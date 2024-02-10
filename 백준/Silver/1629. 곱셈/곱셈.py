def cal(a, b, c):
    if b <= 10:
        return (a ** b) % c
    else:
        return ((cal(a % c, b // 2, c) ** 2) * cal(a % c, b % 2, c)) % c

a, b, c = map(int, input().split())

print(cal(a % c, b, c))