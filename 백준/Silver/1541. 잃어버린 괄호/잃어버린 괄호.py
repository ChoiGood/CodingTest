# # 예쁘게 어떻게 나누지??
numbers = input()

opers = []

# 더 효과적으로 나눌텐데 .. 흠....
i = 0
while True:
    p, m = numbers.find('+', i), numbers.find('-', i)
    if p == -1 and m == -1:
        break

    if p > 0 and m == -1:
        opers.append('+')
        i = p + 1
    elif m > 0 and p == -1:
        opers.append('-')
        i = m + 1
    elif p > 0 and m > 0 and p < m:
        opers.append('+')
        i = p + 1
    elif p > 0 and m > 0 and p > m:
        opers.append('-')
        i = m + 1
    else:
        print('예외')

numbers = numbers.replace('+', '-')
numbers = list(map(int, numbers.split('-')))
N = len(numbers)
# numbers opers 완성!!!
value = numbers[0]

i = 0
state = '+'
while True:
    if i + 1 >= N:
        break

    if opers[i] == '-':
        state = '-'

    if state == '+':
        value += numbers[i + 1]
    elif state == '-':
        value -= numbers[i + 1]
    else:
        print('오류')
    i += 1
print(value)

