import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, R = map(int, input().split())
visited = [0] * (N+1)
depthList = [-1] * (N+1)
vertices = [[] for i in range(N+1)]
cnt = 1

def dfs(r, depth):
    global cnt
    visited[r] = cnt
    depthList[r] = depth
    for i in vertices[r]:
        if not visited[i]:
            cnt += 1
            dfs(i, depth+1)

for i in range(M):
    u, v = map(int, input().split())
    vertices[u].append(v)
    vertices[v].append(u)

for i in range(N + 1):
    vertices[i].sort(reverse=True)

dfs(R, 0)
sum = 0
for i in range(1,N+1):
    sum += visited[i] * depthList[i]
print(sum)