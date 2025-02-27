import sys
input = sys.stdin.readline
N = int(input())
dp = [[] for _ in range(1000001)] # i를 1로 만드는 데 필요한 최소 길이의 연산 과정
dp[1] = [1]
dp[2] = [2, 1]
dp[3] = [3, 1]

if N > 3:
    for i in range(4, N+1):
        tmp = []
        if i % 3 == 0:
            tmp.append((i//3, 3))
        if i % 2 == 0:
            tmp.append((i//2, 2))
        tmp.append((i-1, 1))
        tmp.sort(key=lambda x: len(dp[x[0]]))    
        dp[i] = [i] + dp[tmp[0][0]]
        
print(len(dp[N])-1) 
for i in dp[N]:
    print(i, end=' ')