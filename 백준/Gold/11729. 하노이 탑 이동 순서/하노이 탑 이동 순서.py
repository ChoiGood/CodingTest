def hanoi(n, src, mid, dst):
    if n == 1:
        print(src, dst)
    else:
        hanoi(n - 1, src, dst, mid)
        hanoi(1, src, mid, dst)
        hanoi(n - 1, mid, src,dst)

k = int(input())
print(2 ** k - 1)
hanoi(k, 1, 2, 3)

