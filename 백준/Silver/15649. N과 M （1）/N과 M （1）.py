def nandm(N, M, n, arr):
    if n == M:
        print(*arr)
    else:
        # 기존 배열을 저장해주기
        tmp = arr[:]
        for i in range(1, N + 1):
            if i not in arr: # 기존 배열에 없으면
                tmp.append(i) # 해당 값을 넣고
                nandm(N, M, n + 1, tmp) # 함수 재귀 호출
                tmp.pop() # 여기서 다시 원래대로 돌리기




N, M = map(int, input().split())

nandm(N, M, 0, [])