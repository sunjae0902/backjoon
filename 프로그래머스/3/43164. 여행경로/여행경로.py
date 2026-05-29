from collections import deque, defaultdict

def solution(tickets):
    info = defaultdict(list)

    for s, e in sorted(tickets):
        info[s].append(e)

    q = deque([(["ICN"], set())]) # 출발지, 도착지 경로 저장

    while q:
        path, used = q.popleft()

        if len(used) == len(tickets):
            return path

        cur = path[-1]

        for i, nxt in enumerate(info[cur]):
            if (cur, nxt, i) in used:
                continue
            q.append((path + [nxt], used | {(cur, nxt, i)}))
    return []