import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 도시 수 
m = int(input()) # 여행 계획 도시 수
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, n+1):
        if tmp[j-1] == 1:
            graph[i].append(j)
travel = deque(list(map(int, input().split())))
visited = [0 for _ in range(n+1)]
q = deque([travel[0]])
visited[travel[0]] = 1
flag = 0
while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = 1
            q.append(nxt)
print("YES" if all(visited[n] for n in travel) else "NO")
            
