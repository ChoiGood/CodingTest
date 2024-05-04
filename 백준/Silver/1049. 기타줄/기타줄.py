import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bestSix = 1001
bestOne = 1001
for _ in range(M):
    sixPrice, onePrice = map(int, input().split())
    
    bestSix = min(bestSix, sixPrice)
    bestOne = min(bestOne, onePrice)

caseA = (N // 6) * bestSix + (N % 6) * bestOne
caseB = (N // 6 + 1) * bestSix
caseC = N * bestOne
result = min(caseA, caseB, caseC)

print(result)