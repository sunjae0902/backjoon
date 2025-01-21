def solution(targets):
    # 끝점 정렬
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    last_end = float('-inf')  # 현재 선택된 마지막 구간의 끝점
    
    for start, end in targets:
        # 현재 구간이 기존 선택된 구간과 겹치지 않는 경우만 선택
        if start >= last_end: # 개구간 포함 x
            answer += 1
            last_end = end  # 현재 구간을 선택
    
    return answer
