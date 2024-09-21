import sys
input = sys.stdin.readline
N,M = map(int,input().split())

list = list(map(int, input().split()))
sum = [0 for i in range(N+1)]
for i in range(N):
    sum[i+1] = sum[i] + list[i]
for i in range(M):
     a,b = map(int, input().split())
     print(sum[b]-sum[a-1])