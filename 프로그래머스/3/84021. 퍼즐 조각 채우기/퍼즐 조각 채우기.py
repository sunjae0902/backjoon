from collections import deque

def normalize(cells): # 최소값 기준으로 정규화
    min_x = min(x for x, y in cells)
    min_y = min(y for x, y in cells)
    return sorted((x - min_x, y - min_y) for x, y in cells)

def rotate(cells): # 90도 회전
    return [(y, -x) for x, y in cells]

def solution(game_board, table):
    answer = 0
    n = len(table)
    move = [(1,0), (-1,0), (0,1), (0,-1)]
    blocks = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and table[i][j]:
                q = deque([(i, j)])
                visited[i][j] = 1
                group = []
                while q:
                    r, c = q.popleft()
                    group.append((r,c))
                    for dx, dy in move:
                        nr, nc = r+dx, c+dy
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and table[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                blocks.append(group)  
    
    empty = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and not game_board[i][j]:
                q = deque([(i, j)])
                visited[i][j] = 1
                group = []
                while q:
                    r, c = q.popleft()
                    group.append((r,c))
                    for dx, dy in move:
                        nr, nc = r+dx, c+dy
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and not game_board[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                empty.append(group)
    used = [0 for _ in range(len(blocks))]            
    for space in empty:
        for i, block in enumerate(blocks):
            if len(space) != len(block) or used[i] :
                continue
            norm_space = set(normalize(space))
            rotate_block = block
            for _ in range(4):
                rotate_block = rotate(rotate_block) # 누적 회전
                if norm_space == set(normalize(rotate_block)):
                    answer += len(block)
                    used[i] = 1
                    break
            if used[i]:
                break
    return answer