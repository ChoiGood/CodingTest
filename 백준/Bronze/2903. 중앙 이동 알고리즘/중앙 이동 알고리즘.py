N = int(input())

base = 3

for _ in range(N - 1):
    base += base - 1

print(base ** 2)
