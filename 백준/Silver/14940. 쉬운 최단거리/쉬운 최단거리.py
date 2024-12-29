import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split()) # 행, 열
arr = [] # 간선 정보 저장 
s = [] 
dijk = [[int(1e9) for _ in range(M)] for _ in range(N)] # 각 노드에서 목적지로 가는 최단 거리 저장

for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(len(tmp)):   
        if tmp[j] == 2:
            s = [i, j]
hq = []
dijk[s[0]][s[1]] = 0 # 시작 정점
heapq.heappush(hq, (0, s))
while hq:
    now = heapq.heappop(hq) # 현재 노드
    i, j = now[1][0], now[1][1]
    vertices = []
    # 경계에 따라 인접 정점 추가하기 (경계 벗어나지 않는 경우에만 추가)
    for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
            vertices.append([ni, nj])
    for n in vertices:
        cost = dijk[i][j] + 1
        if cost < dijk[n[0]][n[1]]:
            dijk[n[0]][n[1]] = cost
            heapq.heappush(hq, (cost, n))
            
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(0, end = ' ')
            continue
        elif dijk[i][j] == int(1e9):
            print(-1, end = ' ')
        else:
            print(dijk[i][j], end = ' ')
    print()