def solution(n, info):
    max_diff = 0
    answer = [-1]
    
    def dfs(idx, arrows_left, ryan_info):
        nonlocal max_diff, answer
        
        # 모든 점수에 대해 순회한 경우
        if idx == 11:
            if arrows_left > 0:
                ryan_info[10] += arrows_left  # 남은 화살은 0점에 몰아줌

            ryan_score, apeach_score = 0, 0
            for i in range(11): # 총점 계산
                if info[i] == 0 and ryan_info[i] == 0:
                    continue
                if ryan_info[i] > info[i]:
                    ryan_score += 10 - i
                else:
                    apeach_score += 10 - i

            diff = ryan_score - apeach_score

            if diff > 0:
                if diff > max_diff: # 최대값 갱신
                    max_diff = diff
                    answer = ryan_info[:]
                elif diff == max_diff:
                    # 같은 점수 차이로 우승일 경우, 가장 낮은 점수를 더 많이 맞힌 경우 우선
                    for i in range(10, -1, -1):
                        if ryan_info[i] > answer[i]:
                            answer = ryan_info[:]
                            break
                        elif ryan_info[i] < answer[i]:
                            break

            if arrows_left > 0:
                ryan_info[10] -= arrows_left  # 모두 처리한 후, 다시 탐색(백트래킹) 
            return

        # 해당 점수 안 쏘는 경우
        dfs(idx + 1, arrows_left, ryan_info[:])

        # 어피치보다 1발 더 쏘는 경우
        need = info[idx] + 1
        if arrows_left >= need:
            ryan_info_copy = ryan_info[:]
            ryan_info_copy[idx] = need
            dfs(idx + 1, arrows_left - need, ryan_info_copy)

    dfs(0, n, [0] * 11)
    return answer
