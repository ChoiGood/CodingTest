N = int(input())
numbers = list(map(int, input().split()))

numbers = list(set(numbers))
numbers.sort()

print(*numbers)