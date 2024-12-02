import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0 for i in range(n)] # arr[i]잔까지 마셨을때 최대 가치
dp[0] = arr[0]

for i in range(n):
    if i == 0:
        dp[i] = arr[0]
    elif i == 1:
        dp[i] = dp[i-1] + arr[i]
    elif i == 2:
        dp[i] = max(dp[i-2]+arr[i], dp[i-1], dp[i-1]-arr[i-2]+arr[i])
    else:
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1])
print(dp[n-1])