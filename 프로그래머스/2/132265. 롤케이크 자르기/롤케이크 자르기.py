from collections import Counter # 원소 개수 카운트(딕셔너리)

def solution(topping):
    answer = 0
    left_set = set()
    right_counter = Counter(topping)

    for t in topping:
        left_set.add(t)
        right_counter[t] -= 1 # 개수 감소, 없으면 0
        if right_counter[t] == 0: # 개수가 0이면 아예 삭제
            del right_counter[t]
        if len(left_set) == len(right_counter):
            answer += 1

    return answer
