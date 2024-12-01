import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
dp = [0] * (K+1) # dp[i]: 합이 i가 되는 경우의 수
dp[0] = 1
for coin in coins: 
    for i in range(coin, K+1): 
       dp[i] += dp[i-coin]
    
print(dp[K])