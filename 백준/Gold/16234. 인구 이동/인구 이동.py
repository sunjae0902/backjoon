import sys
input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(r, c):  # 더 이상 인접한 노드가 없을 때 까지 반복
    stack = [(r, c)]
    union = [(r, c)]
    visited[r][c] = 1
    while stack:
        cr, cc = stack.pop()
        for k in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = cr + k[0], cc + k[1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(arr[cr][cc] - arr[nr][nc]) <= R:
                    visited[nr][nc] = 1
                    union.append((nr, nc))
                    stack.append((nr, nc))
    return union

def find():
    unions = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = dfs(i, j)
                if len(union) != 1:
                    unions.append(union)
    return unions

ans = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    unioned = find()
    if not unioned:
        print(ans)
        break
    for us in unioned:  # 연합이 여러개, 각 연합 마다 인구이동 필요
        p = 0
        for u in us:
            p += arr[u[0]][u[1]]
        for u in us:
            arr[u[0]][u[1]] = p // len(us)
    ans += 1