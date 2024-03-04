# 환상의 짝궁

N = 2 * 10 ** 6
sieve = [0] * (N + 1)
primes = []

for i in range(2, N + 1):
    sieve[i] = i

for i in range(2, N + 1):
    if sieve[i] == 0: continue
    primes.append(i)
    for j in range(i*i, N + 1, i):
        sieve[j] = 0

T = int(input()) # 테스트 케이스의 수

for _ in range(T):
    A, B = map(int, input().split())
    Test = A + B

    # 두 수의 합이 2 또는 3 이면 => 소수의 합으로 표현 x
    if Test == 2 or Test == 3:
        print('NO')
        continue

    # N = 2 * 10 ** 6 이하의 수면 에라토스테네스의 체로 결과 출력
    if Test % 2 == 0: # 합이 짝수면 => 골드 바흐의 추측 "4보다 큰 짝수는 두 홀수 소수의 합으로 표현이 가능하다"
        print('YES')
    else: # 합이 홀수라면
        # 홀수 = 짝수 + 홀수 ==> (짝수가 2 일때만 소수이다!!) 2 + 홀수로 표현됨!!
        if Test + 2 <= N:
            if sieve[Test - 2]:
                print('YES')
            else:
                print('NO')
        else:
            flag = True
            for i in primes:
                if sieve[i]:
                    if (Test - 2) % i == 0:
                        flag = False
                        break
            print('YES' if flag else 'NO')