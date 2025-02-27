import sys
input = sys.stdin.readline
T = int(input())
dp = [0 for _ in range(11)] # i를 1,2,3의 합으로 나타내는 가짓수
dp[1], dp[2], dp[3] = 1,2,4
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in range(T):
    print(dp[int(input())])