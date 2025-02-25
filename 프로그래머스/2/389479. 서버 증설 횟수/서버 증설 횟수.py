def solution(players, m, k):
    answer = 0
    now = 0
    server = []
    for i in range(len(players)):
        server = [s for s in server if s <= i < s+k]
        now = len(server)
        cnt = players[i] // m
        server.extend([i] * (cnt-now))
        answer += max(cnt-now, 0)
    return answer