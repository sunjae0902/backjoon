from collections import defaultdict

def solution(gems):
    n = len(set(gems))
    gems_cnt = defaultdict(int)
    answer = [0, len(gems)-1]
    s = 0
    for e in range(len(gems)):
        gems_cnt[gems[e]] += 1
        
        while len(gems_cnt) == n:
            if e - s < answer[1] - answer[0]:
                answer = [s, e]
                
            gems_cnt[gems[s]] -= 1
            if gems_cnt[gems[s]] == 0:
                del gems_cnt[gems[s]]
            s += 1
    return [answer[0]+1, answer[1] + 1]