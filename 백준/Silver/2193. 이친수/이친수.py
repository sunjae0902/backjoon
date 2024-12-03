import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1) # 1...n자리 이친수 중 전체 경우와, 마지막 자리가 1인 경우 수

for i in range(1, n+1):
    if i == 1:
        dp[i] = [1, 1]
    else:
        dp[i] = [
            dp[i - 1][1] + 2 * (dp[i - 1][0] - dp[i - 1][1]),
            dp[i - 1][0] - dp[i - 1][1],
        ]
print(0 if n == 0 else dp[n][0])