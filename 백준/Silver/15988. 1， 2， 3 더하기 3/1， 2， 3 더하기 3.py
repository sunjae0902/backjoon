import sys
input = sys.stdin.readline
T = int(input())
mod = 1000000009
dp = [0] * (1000001) #n을 나타내는 경우의 수
dp[1] = 1
dp[2] = 2
dp[3] = 4
# 테스트 케이스가 있음 -> 몇번 반복할지 모르니까 시간 초과 및 메모리 초과 주의 !
for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod
       
for i in range(T):
    n = int(input())
    print(dp[n])