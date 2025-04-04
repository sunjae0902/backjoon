from collections import deque
import heapq

def solution(land, height):
    n = len(land)
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    def bfs(start, union_id):
        q = deque([start])
        visited[start[0]][start[1]] = union_id
        unions[union_id].append(start)

        while q:
            x, y = q.popleft()
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                    if abs(land[x][y] - land[nx][ny]) <= height:
                        visited[nx][ny] = union_id # 그룹 id 저장
                        unions[union_id].append((nx, ny))
                        q.append((nx, ny))
    
    visited = [[-1] * n for _ in range(n)]
    unions = []
    union_id = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                unions.append([])
                bfs((i, j), union_id)
                union_id += 1

    pq = []
    in_mst = [False] * union_id
    total_cost = 0
    count = 1  # 포함된 유니온 개수

    # 초기 유니온을 MST에 추가
    in_mst[0] = True
    for x, y in unions[0]:
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                other_id = visited[nx][ny]
                if other_id != 0:  # 다른 유니온과의 경계선이라면
                    cost = abs(land[x][y] - land[nx][ny])
                    heapq.heappush(pq, (cost, other_id))

    # Step 3: 프림 알고리즘으로 최소 비용의 다리 연결 (O(N² log N))
    while pq and count < union_id:
        cost, u = heapq.heappop(pq)
        if in_mst[u]:  # 이미 MST에 포함된 유니온이라면 스킵
            continue

        in_mst[u] = True
        total_cost += cost
        count += 1

        # 새로운 유니온이 MST에 추가됐으므로, 그 유니온의 경계를 우선순위 큐에 추가
        for x, y in unions[u]:
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    other_id = visited[nx][ny]
                    if not in_mst[other_id]:  # 다른 유니온이라면 다리 후보 추가
                        new_cost = abs(land[x][y] - land[nx][ny])
                        heapq.heappush(pq, (new_cost, other_id))

    return total_cost
