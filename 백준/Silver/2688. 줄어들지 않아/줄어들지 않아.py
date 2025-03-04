import sys
input = sys.stdin.readline
T = int(input())
dp = [[0] * 10 for _ in range(65)] # i자리 줄어들지 않는 숫자, 끝이 j로 끝나는 경우 
dp[1] = [1] * 10 

for i in range(2, 65):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])
        
for i in range(T):
    N = int(input())
    # n자리 수가 줄어들지 않는다는 것은, n-1수도 줄어들지 않는다는 것을 의미
    print(sum(dp[N]))