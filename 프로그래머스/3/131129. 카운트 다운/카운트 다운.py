from collections import deque
def solution(target):
    answer = []
    scores = []
    
    scores.append((50, 1))
    for i in range(1, 21):
        scores.append((i, 1))
        scores.append((2*i, 0))
        scores.append((3*i, 0))
        
    q = deque()
    q.append((0, 0, 0)) # 현재 점수, 던진 횟수, 싱글 + 불 횟수
    visited = {} # visited[score]: score를 얻는 데 (최소 던진 횟수, 보너스 수)
    
    while q:
        score, count, bonus = q.popleft()
        if score > target:
            continue
            
        if score in visited:
            if count > visited[score][0]:
                continue
            if count == visited[score][0] and bonus <= visited[score][1]:
                continue
        visited[score] = (count, bonus) #갱신
            
        for s, is_bonus in scores:
            q.append((score+s, count+1, bonus + (1 if is_bonus else 0)))
            
    return visited[target]