import sys
input = sys.stdin.readline

N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))
totalLength = 0
ans = length[0] * price[0]
price[1:] = sorted(price[1:])
for i in range(1,N-1):
    totalLength += length[i]
ans += totalLength * price[i]
print(ans)