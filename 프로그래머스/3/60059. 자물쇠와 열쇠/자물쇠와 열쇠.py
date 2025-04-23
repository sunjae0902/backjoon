def rotate(arr, d): 
    N = len(arr)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1: # 90도 회전: r행은 N-r-1열, c열은 c행
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = arr[r][c]
    elif d % 4 == 2: # 180: 상하, 좌우 반전
        for r in range(N):
            for c in range(N):
                ret[N-1-c][N-1-r] = arr[r][c]
    elif d % 4 == 3: # 270: 90도랑 반대로
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = arr[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = arr[r][c]
    return ret

def check(key, lock, dx, dy):
    N, M = len(lock), len(key)
    for i in range(N):
        for j in range(N):
            ki = i - dx # lock 기준이므로 key 기준으로 보정해야함
            kj = j - dy
            if 0 <= ki < M and 0 <= kj < M:
                if key[ki][kj] + lock[i][j] != 1: # 홈이 맞지 않을 경우
                    return False
            else:
                if lock[i][j] == 0: # 비어있으면 안 됨
                    return False
    return True
    
def solution(key, lock):
    answer = False
    stack = [key]
    visited = set()
    N, M = len(lock), len(key)
                
    while stack:
        now_key = stack.pop()
        
        key_tuple = tuple(map(tuple, now_key))
        if key_tuple in visited:
            continue
        visited.add(key_tuple)
        
        for dx in range(-M+1, N): # 이동 범위 제한 없음, 좌표 기준 최소 한 칸은 겹쳐야하므로 -M+1~N-1
            for dy in range(-M+1, N):
                if check(now_key, lock, dx, dy):
                    return True
                
        for d in range(1, 4):
            rotated = rotate(now_key, d)
            stack.append(rotated)
   
    return answer