import sys
input = sys.stdin.readline

N, K = map(int,input().split())
bp = [(0,0)] * (N+1)
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
# dp[n][k] : n번째 아이템까지 포함, 무게 k 이하일 경우 최대 가치
for i in range(1, N+1):
    W, V = map(int, input().split())
    bp[i] = (W, V)

for i in range(1, N+1):
    w, v = bp[i]
    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[N][K])