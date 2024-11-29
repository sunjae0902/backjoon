import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]  # 인접 리스트에 간선 정보 저장 (튜플 저장)
distances = [INF] * (N+1) # 시작 노드 X부터 모든 정점까지의 최단거리 

for i in range(M):
    s, e = map(int, input().split())
    arr[s].append((e, 1))
    
# Priority Queue
def dijkstra_2(s):
    hq = []
    distances[s] = 0
    # 시작 노드로 가는 최단 경로 0, 큐에 삽입
    heapq.heappush(hq, (0, s))
    while hq:
        dist, now = heapq.heappop(hq) # 최단 거리인 노드를 꺼내기 (최소 힙)
       
        for i, c in arr[now]:
            cost = distances[now] + c
            if cost < distances[i]:
                distances[i] = cost
                heapq.heappush(hq, (cost, i))
    
dijkstra_2(X)

flag = 0
for i in range(len(distances)):
    if distances[i] == K:
        print(i)
        flag = 1
if not flag:
    print(-1)