from collections import defaultdict
# 여집합
def solution(clothes):
    answer = 0
    closet = defaultdict(list)
    for c in clothes:
        closet[c[-1]].append(c[0])
    cnt = 1
    for v in closet.values():
        cnt *= len(v)+1
    answer = cnt-1
    return answer