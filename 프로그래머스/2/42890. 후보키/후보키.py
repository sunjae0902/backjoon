from itertools import combinations
from collections import defaultdict

def solution(relation):
    rows = len(relation)
    cols = [i for i in range(len(relation[0]))]
    candidates = set()
    answer = 0
    for i in cols:
        for combi in combinations(cols, i+1): # 후보 키 조합
            if any(set(candidate).issubset(combi) for candidate in candidates):
                continue
            info = defaultdict(int)
            keys = [[] for _ in range(rows)]
            for c in combi:
                for r in range(rows):
                    keys[r].append(relation[r][c])
            for k in keys:
                info[tuple(k)] += 1
            flag = 1
            for k, v in info.items():
                if v > 1:
                    flag = 0
                    break
            if flag:
                answer += 1
                candidates.add(combi)
    return answer