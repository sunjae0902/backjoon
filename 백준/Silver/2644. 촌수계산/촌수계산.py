import sys
input = sys.stdin.readline
n = int(input())

# dfs에서 두 사람 간의 거리를 구하면 됨.
target = list(map(int, input().split()))
m = int(input())
rel = [[] for _ in range(n+1)]
visited = [0 for _ in range(n + 1)]
res = []

def dfs(s, cnt):
    if s == target[1]:
        return cnt
    visited[s] = 1
    for v in rel[s]: # 인접 노드 계산
        if not visited[v]:
            res = dfs(v, cnt+1) # 카운트 증가
            if res != -1:
                return res
    return -1

for i in range(m): # 양방향으로 저장
    p, c = map(int, input().split())
    rel[p].append(c)
    rel[c].append(p)
    
print(dfs(target[0], 0))