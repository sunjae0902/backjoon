from collections import defaultdict

def solution(clothes):
    answer = 1
    d = defaultdict(list)
    for n, t in clothes:
        d[t].append(n)
    for val in d.values():
        answer *= len(val) + 1
    return answer-1