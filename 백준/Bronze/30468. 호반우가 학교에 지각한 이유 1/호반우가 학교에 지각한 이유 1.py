STR, DEX, INT, LUK, N = map(int, input().split())
totalStat = STR + DEX + INT + LUK

print(0 if totalStat >= 4*N else 4 * N - totalStat)