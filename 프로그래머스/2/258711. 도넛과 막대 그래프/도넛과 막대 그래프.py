from collections import defaultdict
def solution(edges): # 도넛, 막대, 8자 그래프를 찾는다
    # 막대 0111110 구조
    # 도넛 1111111 구조
    # 8자  112111 11132111 구조
    answer = [0,0,0,0]
    inout = defaultdict(lambda: [0, 0])  # 기본값 [0, 0] 설정, 각 노드의 진입/진출 차수
    vertices = defaultdict(set) # 인접 정점 저장
    for e in edges:
        inout[e[0]][1] += 1
        inout[e[1]][0] += 1
        vertices[e[0]].add(e[1])
        vertices[e[1]].add(e[0])
    for k in inout.keys(): # 가운데 정점 찾기
        if inout[k][1] - inout[k][0] >= 2:
            answer[0] = k
            break
    for e in edges:
        if e[0] == answer[0]:
            q = [e[1]]
            visited = set()
            visited.add(e[1])
            res = [inout[e[1]][0]-1, inout[e[1]][1]] # 가운데 정점으로부터의 진입차수 하나 빼주기
            while q:
                n = q.pop()
                for v in vertices[n]:
                    if v != e[0] and v not in visited:
                        visited.add(v)
                        q.append(v)
                        res.extend(inout[v])
            min_val, max_val = min(res), max(res)
            if min_val == 0: # 최소값이 0이라면, 막대 그래프
                answer[2] += 1
                continue
            elif max_val == 1: # 최대값이 1이라면, 도넛 그래프
                answer[1] += 1
            else: # 그 외: 8자 그래프
                answer[3] += 1                       
    return answer