import sys
input = sys.stdin.readline

# 오른쪽, 아래, 대각선 이동

N, M = map(int, input().split())
arr = [[] for _ in range(M) for _ in range (N)]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
# (i,j)에서 최대값

for i in range(N):
    arr[i] = list(map(int, input().split()))
    
for i in range(1, N+1):
    for j in range(1, M+1):
        if j == 1:
            dp[i][j] = dp[i-1][j] + arr[i-1][j-1]
        if i == 1:
            dp[i][j] = dp[i][j-1] + arr[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + arr[i-1][j-1]

print(dp[N][M])