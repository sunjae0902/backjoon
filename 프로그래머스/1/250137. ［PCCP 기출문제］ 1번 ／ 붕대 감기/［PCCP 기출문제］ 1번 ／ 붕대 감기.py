def solution(bandage, health, attacks):
    answer = health
    cnt = 0
    i = 0
    j = 0
    max_time = attacks[-1][0]

    while i <= max_time:
        if j < len(attacks) and i == attacks[j][0]:
            cnt = 0
            answer -= attacks[j][1]
            if answer <= 0:
                return -1
            j += 1
        else:
            answer += bandage[1]
            cnt += 1
            if cnt == bandage[0]:
                answer += bandage[2]
                cnt = 0
            answer = min(answer, health) # 최대값 넘지 x
        i += 1
    return answer