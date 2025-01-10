import sys
from collections import defaultdict
input = sys.stdin.readline
H, W = map(int, input().split())
block = list(map(int, input().split()))
arr = [[0 for _ in range(W)] for _ in range(H)]
for i in range(W):
    for j in range(block[i]):
        arr[H-j-1][i] = 1
cnt = 0
for i in range(H):
    interval = []
    for j in range(W):
        if arr[i][j] == 1:
            interval.append(j)
    if len(interval) < 2 or len(interval) == W:
        continue
    for k in range(len(interval)-1):
        cnt += interval[k:k+2][-1] - interval[k:k+2][0] - 1
print(cnt)