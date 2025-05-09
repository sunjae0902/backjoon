import sys
sys.setrecursionlimit(100000)
def solution(n, lighthouse):
    graph = [[] for _ in range(n+1)]
    for s, e in lighthouse:
        graph[s].append(e)
        graph[e].append(s)
    
    visited = [0] * (n+1)
    dp = [[0,0] for _ in range(n+1)]
    
    def dfs(node):
        visited[node] = 1
        dp[node][0] = 0 # 현재 노드가 꺼진 경우 최소 등대 수
        dp[node][1] = 1 # 현재 노드가 켜진 경우 최소 등대 수
        for child in graph[node]:
            if not visited[child]:
                dfs(child)
                dp[node][0] += dp[child][1]
                dp[node][1] += min(dp[child][0], dp[child][1])
    dfs(1)
    return min(dp[1][0], dp[1][1]) # 루트노드기준