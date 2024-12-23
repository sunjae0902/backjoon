import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[int(1e9)] * 3 for _ in range(M)] for _ in range(N)]
# 모든 가능한 방향에서의 값을 저장해두었다가, 조건에 맞게 최솟값을 구해야 함 (최솟값 먼저 구하지 않고)
for i in range(N):
    for j in range(M):
        if i == 0:
            dp[i][j] = [arr[i][j]] * 3
            continue
        if j == 0:
            for k in [1, 2]:
                for d in range(3):
                    if d != k and dp[i][j][k] > dp[i-1][j+k-1][d] + arr[i][j]:
                        dp[i][j][k] = dp[i - 1][j + k - 1][d] + arr[i][j]
        elif j == M-1:
            for k in [0, 1]:
                for d in range(3):
                    if d != k and dp[i][j][k] > dp[i - 1][j + k - 1][d] + arr[i][j]:
                        dp[i][j][k] = dp[i - 1][j + k - 1][d] + arr[i][j]
        else:
            for k in [0, 1, 2]:
                for d in range(3):
                    if d != k and dp[i][j][k] > dp[i - 1][j + k - 1][d] + arr[i][j]:
                        dp[i][j][k] = dp[i - 1][j + k - 1][d] + arr[i][j]
ans = int(1e9)
for i in dp[N-1]:
    ans = min(ans, min(i))
print(ans)