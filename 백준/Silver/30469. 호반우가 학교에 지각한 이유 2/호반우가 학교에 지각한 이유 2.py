# 호반우가 학교에 지각한 이유2

# sieve = [0] * 101
# primes = []

# for i in range(2, 101):
#     sieve[i] = i

# for i in range(2, 101):
#     if sieve[i] == 0:
#         continue
#     primes.append(i)
#     for j in range(i*i, 101, i):
#         sieve[j] = 0

a, b, n = input().split()
n = int(n)
forPrimeSword = ['1', '3', '7', '9']

if a[-1] in forPrimeSword and b[0] in forPrimeSword:
    if a[-1] == '9':
        result = a + '7' + '1' * (n - 5) + b
    else:
        result = a + '1' * (n - 4) + b
    print(result)
else:
    print(-1)