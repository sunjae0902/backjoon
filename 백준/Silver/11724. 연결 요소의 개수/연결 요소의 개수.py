import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N,M = map(int,input().split())

visited = [0] * (N + 1)
vertices = [[] for i in range(N + 1)]
cnt = 0

def dfs(r):
    visited[r] = 1
    for i in vertices[r]:
        if not visited[i]:
            dfs(i)
    
for i in range(M):
    u, v = map(int, input().split())
    vertices[u].append(v)
    vertices[v].append(u)
    
for i in range(1, N+1):
    if not visited[i]: # 조건 명시
        dfs(i)
        cnt += 1
print(cnt)