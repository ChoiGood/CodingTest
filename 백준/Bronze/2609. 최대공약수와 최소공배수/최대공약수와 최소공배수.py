import math

a, b = map(int, input().split())

common_div = math.gcd(a, b)
print(common_div)
print(int(a * b / common_div))