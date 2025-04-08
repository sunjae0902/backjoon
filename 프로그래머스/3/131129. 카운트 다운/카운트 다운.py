from collections import deque

def solution(target):
    scores = []

    for i in range(1, 21):
        scores.append((i, 1))   # single, Bull인 경우만 우선순위 
        scores.append((i * 2, 0)) 
        scores.append((i * 3, 0))
    scores.append((50, 1))

    # BFS: (현재 점수, 던진 횟수, 싱글+불 횟수)
    queue = deque()
    queue.append((0, 0, 0))  # 시작점

    # visited[score] = (최소 던진 횟수, 보너스 사용 횟수)
    visited = {}

    while queue:
        cur, count, bonus = queue.popleft()

        if cur > target:
            continue

        # 이미 방문한 점수인 경우 → 더 적은 횟수로 방문했다면 갱신 안 함
        if cur in visited:
            prev_count, prev_bonus = visited[cur]
            if count > prev_count:
                continue
            if count == prev_count and bonus <= prev_bonus:
                continue

        visited[cur] = (count, bonus)

        # 다음 점수 탐색
        for score, is_bonus in scores:
            queue.append((cur + score, count + 1, bonus + is_bonus))

    # 결과
    min_count, max_bonus = visited[target]
    return [min_count, max_bonus]
