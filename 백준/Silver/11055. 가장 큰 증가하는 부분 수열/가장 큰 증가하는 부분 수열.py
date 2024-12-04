import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N+1) # dp[i] => i 원소를 마지막으로 추가했을때 증가하는 부분수열 중 최대합 저장

dp[1] = arr[0]

for i in range(2, N+1):
    last = arr[i-1] 
    for j in range(i-1):  
        if arr[j] < last:
            dp[i] = max(dp[i], last + dp[j+1])
        else:
            dp[i] = max(dp[i], last)

print(max(dp))