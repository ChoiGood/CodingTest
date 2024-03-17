T = int(input()) # 테스트 케이수 수

for _ in range(T):
    N = int(input()) # 소설을 구성하는 장의 수
    arr = [0] + list(map(int, input().split()))

    # S[i]는 1번 부터 i번까지의 누적합
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i-1] + arr[i]

    # dp[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # dp[i][k] + dp[N+1][j] + sum(A[i]~A[j])
    dp = [[0] * (N+1) for _ in range(N+1)]
    ## 이부분 니가 짜봐라 => 대각선으로 만들어야함
    for i in range(2, N+1): # 부분 파일의 길이
        for j in range(1, N-i+2):   # 시작점
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])
    print(dp[1][N])