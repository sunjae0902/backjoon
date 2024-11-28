# bfs
import sys, queue
input = sys.stdin.readline

N, M, R = map(int, input().split())
visited = [0] * (N+1)
vertices = [[] for i in range(N+1)]


for i in range(M):
    u, v = map(int, input().split())
    vertices[u].append(v)
    vertices[v].append(u)
    
for i in range(N+1):
    vertices[i].sort()
    
myq = queue.Queue()
# get / put method
def bfs(r):
    cnt = 1
    visited[r] = cnt
    myq.put(r)
    while myq.qsize() > 0:
        u = myq.get()
        for v in vertices[u]:
            if not visited[v]:
                cnt += 1
                visited[v] = cnt
                myq.put(v)
                
bfs(R)

for i in range(1, N+1):
    print(visited[i])