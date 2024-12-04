import sys
input = sys.stdin.readline

N = int(input())
dp = [[1] * 10] * (N+1) # n자리 수 오르막 수 중 끝자리가 i인 개수

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
ans = 0
for i in range(10):
    ans += dp[N][i]
print(ans % 10007)