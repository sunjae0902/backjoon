import sys
sys.setrecursionlimit(10**9)  # 재귀 깊이
input = sys.stdin.readline
input = sys.stdin.readline
N, M, R = map(int, input().split())
visited = [-1] * (N + 1) # -1로  초기화
vertices = [[] for i in range(N + 1)]


def dfs(r,depth):  # 시작 정점
    visited[r] = depth
    for i in vertices[r]:
        if visited[i] == -1: # 방문 x
            dfs(i, depth+1)


for i in range(M):
    u, v = map(int, input().split())
    vertices[u].append(v)
    vertices[v].append(u)

for i in range(N + 1):
    vertices[i].sort()

dfs(R, 0)
# 정점의 깊이 출력하기
for i in range(1, N + 1):
    print(visited[i])