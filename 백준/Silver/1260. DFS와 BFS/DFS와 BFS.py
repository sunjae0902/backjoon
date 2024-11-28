import sys, queue
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, R = map(int, input().split())
visited = [0] * (N+1)
vertices = [[] for i in range(N+1)]
myq = queue.Queue()

for i in range(M):
    u, v = map(int, input().split())
    vertices[u].append(v)
    vertices[v].append(u)
for i in range(N+1):
    vertices[i].sort()
    
def dfs(r):
    print(r, end = ' ')
    visited[r] = 1
    for i in vertices[r]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)
    
def bfs(r):
    visited[r] = 1
    myq.put(r)
    print(r, end = ' ')
    while myq.qsize() > 0:
        u = myq.get()
        for i in vertices[u]:
            if not visited[i]:
                print(i, end = ' ')
                visited[i] = 1
                myq.put(i)

dfs(R)
visited = [0] * (N+1)
print()
bfs(R)