from collections import deque

def solution(places):
    answer = []
    n = len(places)
    
    for place in places:
        res = 1
        for i in range(n):
            place[i] = list(place[i])
            for j in range(n):
                if place[i][j] != 'P':
                    continue
                q = deque([(i, j, 0)])
                visited = [[0 for _ in range(n)] for _ in range(n)]
                visited[i][j] = 1
                
                while q:
                    r, c, d = q.popleft()
                    if d > 2:
                        continue
                        
                    if d > 0 and place[r][c] == 'P':
                        res = 0
                        break
                    
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = r + dx
                        ny = c + dy

                        if not (0 <= nx < n and 0 <= ny < n):
                            continue

                        if visited[nx][ny]:
                            continue

                        # 파티션은 통과할 수 없음
                        if place[nx][ny] == 'X':
                            continue

                        visited[nx][ny] = 1
                        q.append((nx, ny, d + 1))
        answer.append(res)
    
    return answer