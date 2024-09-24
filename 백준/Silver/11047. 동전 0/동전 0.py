import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
coins.reverse()
cnt = 0
for i in range(N):
    if K // coins[i] < 1:
        continue
    else:
        cnt += K // coins[i]
        K = K % coins[i] 
print(cnt)