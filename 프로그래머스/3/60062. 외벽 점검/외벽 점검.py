from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak)
    weak_extended = weak + [w + n for w in weak]  # 선형화
    answer = len(dist) + 1  
    
    for i in range(1, len(dist) + 1): 
        for friends in permutations(dist, i):
            for start in range(weak_len):  # 시작점
                count = 0
                position = weak_extended[start] + friends[count]  # 처음에 커버 가능한 최대 위치
                
                for idx in range(start, start + weak_len):
                    if weak_extended[idx] > position: # 커버 못 함
                        count += 1
                        if count >= i:
                            break
                        position = weak_extended[idx] + friends[count]
                else: # for문이 끝까지 돌았을 경우(모든 지점 탐지) 실행
                    answer = min(answer, i)

    return answer if answer <= len(dist) else -1
