import heapq as hq

def solution(cards): # 완전 탐색 후, 상위 2 그룹을 추출
    answer = 0
    q = []
    visited = [0] * (len(cards))
    for i in range(len(cards)):
        if visited[i]:
            continue
        visited[i] = 1
        link, cur = 1, i
        while cards[cur] != i+1: # 열어야 할 상자가 이미 열려있을 때까지.
            cur = cards[cur] - 1
            visited[cur] = 1  
            link += 1
        hq.heappush(q, -link)
    if len(q) >= 2:
        answer = hq.heappop(q) * hq.heappop(q)
    return answer