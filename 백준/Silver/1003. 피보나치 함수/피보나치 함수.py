import sys
input = sys.stdin.readline
T = int(input())
arr = [int(input()) for _ in range(T)]

dp = [[]] * 41
   
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i] = [dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]]
    
for i in arr:
    print(dp[i][0], dp[i][1])