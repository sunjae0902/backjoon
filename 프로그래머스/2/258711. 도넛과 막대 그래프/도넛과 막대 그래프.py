from collections import defaultdict
def solution(edges): # 도넛, 막대, 8자 그래프를 찾는다
    # 막대 0111110 구조
    # 도넛 1111111 구조
    # 8자  112111 11132111 구조
    answer = [0,0,0,0]
    inout = defaultdict(lambda: [0, 0])  # 기본값 [0, 0] 설정, 진입/진출 차수
    vertices = defaultdict(set)
    for e in edges:
        inout[e[0]][1] += 1
        inout[e[1]][0] += 1
        vertices[e[0]].add(e[1])
        vertices[e[1]].add(e[0])
    for k in inout.keys():
        if inout[k][1] - inout[k][0] >= 2:
            answer[0] = k
            break
    for e in edges:
        if e[0] == answer[0]:
            q = [e[1]]
            visited = set()
            visited.add(e[1])
            res = [inout[e[1]][0]-1, inout[e[1]][1]]
            while q:
                n = q.pop()
                for v in vertices[n]:
                    if v != e[0] and v not in visited:
                        visited.add(v)
                        q.append(v)
                        res.extend(inout[v])
            min_val, max_val = min(res), max(res)
            if min_val == 0:
                answer[2] += 1
                continue
            elif max_val == 1:
                answer[1] += 1
            else:
                answer[3] += 1                       
    return answer