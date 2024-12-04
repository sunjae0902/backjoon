import sys, math
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
dp = [INF] * (N+1) # 제곱수의 합이 i일때 제곱수들의 항의 최소개수
dp[0] = 0
dp[1] = 1

for i in range(2, N+1):
    for j in range(1, int(math.sqrt(i))+1):
        if j**2 == i:
            dp[i] = 1
        else:
            dp[i] = min(dp[i], dp[i-j**2]+1)
print(dp[N]) 