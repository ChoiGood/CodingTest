# 숫자의 신
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
numbers = [input().rstrip() for _ in range(K)] # K 개의 숫자들

# 1. 가장 큰 수를 만들 수 있는 N개의 숫자 뽑기 (각각 1개는 사용해야한다.)
# numbers 정렬 후 수의 개수를 지정하자 (정렬 기준 : 1. 자리 수 (내림차순) 2. 값 (내림차순))
numbers.sort(key=lambda x: (-len(x), -int(x)))

# 가장 큰 숫자를 만들기 위해서는 자릿 수가 가장 커야하고 동일한 자릿수라면 값이 크면 된다.
# 숫자를 중복해서 뽑을 수 있기 때문에 정렬 후 기준을 만족하는 수를 중복해서 넣어주자
mx_num = numbers[0]
mx_len = len(numbers[0])
for _ in range(N - K):
    numbers.append(mx_num)

# 2. 뽑은 N개의 숫자를 가장 크게 조합
# 정렬을 수행하여 구현
numbers.sort(key = lambda x: x*9, reverse=True)

print(''.join(numbers))