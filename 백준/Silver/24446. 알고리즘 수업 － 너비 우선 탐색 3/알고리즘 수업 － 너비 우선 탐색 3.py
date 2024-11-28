# bfs
import sys, queue
input = sys.stdin.readline

N, M, R = map(int, input().split())
visited = [-1] * (N+1)
vertices = [[] for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    vertices[u].append(v)
    vertices[v].append(u)
myq = queue.Queue()

def bfs(r):
    cnt = 0
    visited[r] = cnt
    myq.put(r)
    while myq.qsize() > 0:
        u = myq.get()
        for v in vertices[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1 # 부모 + 1
                myq.put(v)
bfs(R)

for i in range(1, N+1):
    print(visited[i])