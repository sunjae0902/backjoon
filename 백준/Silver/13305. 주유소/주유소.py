import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_price = int(10e9)
res = 0
for i in range(N-1):
    min_price = min(min_price, cost[i])
    res += min_price * dist[i]
print(res)