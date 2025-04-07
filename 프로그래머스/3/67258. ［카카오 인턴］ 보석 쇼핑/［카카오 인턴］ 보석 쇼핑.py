from collections import defaultdict
    
def solution(gems):
    total_types = len(set(gems))  # 모든 종류 수
    gem_counter = defaultdict(int)
    answer = [0, len(gems) - 1]
    s = 0

    for e in range(len(gems)):
        gem_counter[gems[e]] += 1 # 갯수 업데이트

        while len(gem_counter) == total_types: 
            if e - s < answer[1] - answer[0]: # 모든 종류 포함 -> 최솟값 갱신
                answer = [s, e]

            gem_counter[gems[s]] -= 1
            if gem_counter[gems[s]] == 0:
                del gem_counter[gems[s]]
            s += 1

    return [answer[0] + 1, answer[1] + 1]
