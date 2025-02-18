from itertools import combinations
def solution(n, q, ans):
    answer = 0
    m = len(q)
    arr = [i for i in range(1, n+1)]
    
    for comb in combinations(arr, 5):
        comb = set(comb)
        flag = 1
        for i in range(m):
            if len(comb.intersection(set(q[i]))) != ans[i]:
                flag = 0
                break
        if flag:
            answer += 1
    return answer