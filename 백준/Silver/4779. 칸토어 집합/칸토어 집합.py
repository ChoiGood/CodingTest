def cantoa(n):
    if n == 1:
        return '-'
    else:
        return cantoa(n // 3) + ' ' * (n//3) + cantoa(n // 3)

while True:
    try:
        N = int(input())
        print(cantoa(3 ** N))
    except EOFError:
        break

