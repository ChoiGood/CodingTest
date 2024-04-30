a, b = map(int, input().split())
a, b = a-1, b-1
result = abs(a // 4 - b // 4) + abs(a % 4 - b % 4)
print(result) 