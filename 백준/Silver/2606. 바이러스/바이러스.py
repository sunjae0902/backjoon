import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
visited = [0] * (N+1)
vertices = [[] for i in range(N+1)]
cnt = 0

def dfs(r):
    global cnt
    visited[r] = 1
    for i in vertices[r]:
        if not visited[i]:
            cnt += 1
            dfs(i)

for i in range(M):
    u,v = map(int, input().split())
    vertices[u].append(v)
    vertices[v].append(u)

dfs(1)
print(cnt)