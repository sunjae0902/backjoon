import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
res = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
for i in range(N):
    for j in  range(N):
        res[i+1][j+1] = res[i][j+1] + res[i+1][j] - res[i][j] + arr[i][j]
for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    print(res[x2][y2] - res[x1-1][y2] - res[x2][y1-1] + res[x1-1][y1-1])
