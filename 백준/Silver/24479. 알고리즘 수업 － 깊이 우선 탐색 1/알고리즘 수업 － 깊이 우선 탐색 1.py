import sys
sys.setrecursionlimit(10**9) # 재귀 깊이
input = sys.stdin.readline
N, M, R = map(int, input().split())
visited = [0] * (N+1)
vertices = [[] for i in range(N+1)]
cnt = 1

def dfs(r): # 시작 정점
    global cnt
    visited[r] = cnt
    for i in vertices[r]:
        if not visited[i]:
            cnt += 1
            dfs(i)

for i in range(M):
    u, v = map(int, input().split())
    vertices[u].append(v)
    vertices[v].append(u)

for i in range(N+1):
    vertices[i].sort()

dfs(R)
# 정점이 아니라, i번째 노드의 순서를 출력하는 것
for i in range(1,N+1):
    print(visited[i])