from collections import deque
def solution(cost, hint):
    answer = int(1e9)
    n = len(cost)
    q = deque([(0, 0, [])]) # 스테이지, 비용, 보유한 힌트번들
    visited = [[0, 0] for _ in range(n)]
    while q:
        stage, cur_cost, hints = q.popleft()
        cur_cost += cost[stage][min(hints.count(stage+1), n-1)]
        if stage == n-1:
            answer = min(answer, cur_cost)
        else:
            q.append((stage+1, cur_cost, hints))
            bundle = hint[stage]
            new_hint = hints[::] + bundle[1:]
            q.append((stage+1, cur_cost + bundle[0], new_hint))
    return answer