import sys
input = sys.stdin.readline
N,K = map(int,input().split())
list = list(map(int, input().split()))
res = [0 for i in range(N-K+2)]
sum = [0 for i in range (N+1)]

for i in range(N):
    sum[i+1] = sum[i]+list[i]
for i in range(1,N-K+2):
   res[i] = sum[i+K-1] - sum[i-1]
print(sorted(res[1:],reverse=True)[0])