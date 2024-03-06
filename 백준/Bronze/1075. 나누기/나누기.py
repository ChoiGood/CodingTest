# 나누기
n1 = int(input())
n2 = int(input())

share = n1 // 100
value = share * 100
for i in range(100):
    if (value + i) % n2 == 0:
        break

print(i if i >= 10 else '0' + str(i))