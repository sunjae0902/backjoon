import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    min_cost = min(graph[s][e], c)
    graph[s][e] = min_cost

for i in range(1, n+1): # 중간 노드
    for j in range(1, n+1):
        for k in range(1, n+1):
            if j == k:
                continue
            min_cost = min(graph[j][k], graph[j][i] + graph[i][k])
            graph[j][k] = min_cost
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != int(1e9):
            print(graph[i][j], end=' ')
        else:
            print(0, end=' ')
    print()