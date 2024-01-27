import sys
N, M = map(int, input().split())

poket_To_num = {}
num_To_poket = {}

for i in range(1, N + 1):
    temp_str = sys.stdin.readline().rstrip()
    poket_To_num[temp_str] = i
    num_To_poket[i] = temp_str

for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    try:
        num = int(temp)
        print(num_To_poket[num])
    except ValueError:
        print(poket_To_num[temp])
