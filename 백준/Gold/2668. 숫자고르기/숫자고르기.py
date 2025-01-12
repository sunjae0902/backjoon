import sys
input = sys.stdin.readline
N = int(input())
# dfs, 사이클을 구성하는 노드를 찾기
ans = []
arr = [[] for _ in range(N+1)]

for i in range(N):
    arr[int(input())].append(i+1)
    
for i in range(1, N+1):
    visited = [0] * (N+1)
    s = [i] # 현재 방문 노드
    visited[i] = 1
    
    while s:
        now = s.pop()
        for v in arr[now]:
            if not visited[v]:
                s.append(v)
                visited[v] = 1
            elif i == v: # 시작 노드로 돌아옴
                ans.append(v)
ans.sort()
print(len(ans))
for i in ans:
    print(i)