import sys
input = sys.stdin.readline
T = int(input())

def solve(s, conv, e):
    visited = [0] * (len(conv) + 2)
    visited[0] = 1
    def dfs(s): 
        if abs(s[0]-e[0]) + abs(s[1]-e[1]) <= 1000:
            visited[-1] = 1
            return 
        for i in range(len(conv)):
            nx, ny = conv[i][0], conv[i][1]
            if not visited[i+1] and abs(nx-s[0]) + abs(ny-s[1]) <= 1000:
                visited[i+1] = 1
                dfs([nx, ny])
    dfs(s)
    print('happy' if visited[-1] == 1 else 'sad')

for _ in range(T):
    n = int(input())
    s = list(map(int, input().split()))
    conv = [list(map(int,input().split())) for _ in range(n)]
    e = list(map(int, input().split()))
    solve(s, conv, e)