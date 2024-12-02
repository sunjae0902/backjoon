import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N+1)] # arr[i]를 마지막으로 저장했을 때, 증가하는 부분수열의 최대 길이 

for i in range(2, N+1):
    last = arr[i-1] 
    for j in range(i-1):
        if arr[j] < last:
            dp[i] = max(dp[i], dp[j+1]+1)
       
print(max(dp))
             