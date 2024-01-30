N = int(input())
rainbow_list = set()
rainbow_list.add('ChongChong')

for _ in range(N):
    A, B = input().split()
    if (A in rainbow_list) or (B in rainbow_list):
        rainbow_list.add(A)
        rainbow_list.add(B)
print(len(rainbow_list))