from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for cnt in course:
        comb_cnt = defaultdict(int)
        for order in orders:
            for comb in combinations(list(order), cnt):
                comb_cnt[tuple(sorted(comb))] += 1
        max_comb = sorted([item for item in comb_cnt.items() if item[1] > 1], reverse = True, key = lambda x: x[1])
        
        for comb in max_comb:
            if comb[1] < max_comb[0][1]:
                break
            answer.append(''.join(sorted(comb[0])))

    return sorted(answer)