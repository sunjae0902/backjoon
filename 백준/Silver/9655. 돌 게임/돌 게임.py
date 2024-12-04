import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * (N+2) # 돌이 i개있을 때 게임이 끝나는 턴, 홀수라면 상근, 짝수라면 창영 윈
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = min(dp[i-1] + 1, dp[i-3] + 1)

print("SK" if dp[N] % 2 != 0 else "CY")