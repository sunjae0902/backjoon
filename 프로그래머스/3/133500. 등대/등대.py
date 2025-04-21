import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

def solution(n, lighthouse):
    graph = defaultdict(list)
    
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    dp = [[0, 0] for _ in range(n + 1)] # 서브트리 루트 노드가 꺼지거나 켜진 경우 서브트리의 최소 등대 수
    visited = [0] * (n + 1)

    def dfs(node):
        visited[node] = 1
        dp[node][0] = 0  # node off
        dp[node][1] = 1  # node on
        for child in graph[node]:
            if not visited[child]:
                dfs(child)
                dp[node][0] += dp[child][1] # 현재 노드가 꺼지면 -> 자식 노드가 무조건 켜져야 함
                dp[node][1] += min(dp[child][0], dp[child][1]) # 현재 노드 켜짐 -> 두 상태 중 최솟값 선택

    dfs(1)
    return min(dp[1][0], dp[1][1])
