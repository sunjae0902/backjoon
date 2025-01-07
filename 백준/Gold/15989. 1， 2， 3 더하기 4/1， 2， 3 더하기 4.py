import sys
input = sys.stdin.readline
T = int(input())
dp = [1 for _ in range(10001)] # 1로만 사용

# 숫자를 사용하는 순서를 강제하여 구성이 중복되는 경우를 무시함.
for i in range(2, 10001): # 2를 사용하는 경우
    dp[i] += dp[i-2]
for i in range(3, 10001): # 3을 사용하는 경우
    dp[i] += dp[i-3]

for i in range(T):
    N = int(input())
    print(dp[N])