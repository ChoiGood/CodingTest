# 이항 계수3
# 페르마의 소정리를 이용하여 계산!!

# 펙토리얼 dp 구현
fac = [i for i in range(4000001)]
fac[0] = 1
for i in range(1, 4000001):
    fac[i] = (fac[i] * fac[i - 1]) % 1000000007

def fpow(base, exp):
    if exp < 0:
        print('양수만 처리하는 함수입니다')
    elif exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        x = fpow(base, exp // 2)
        if exp % 2 == 0:
            return (x * x) % 1000000007
        else:
            return (x * x * base) % 1000000007



# 이항 계수
N, K = map(int, input().split())

result = (fac[N] * fpow((fac[K] * fac[N - K]) % 1000000007, 1000000007 - 2)) % 1000000007 

print(result)