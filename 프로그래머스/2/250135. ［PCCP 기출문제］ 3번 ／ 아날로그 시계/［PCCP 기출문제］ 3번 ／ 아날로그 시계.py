def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2
    
    if start_time == 0 or start_time == 12 * 60 * 60: # 0시00분00초, 12시00분00초는 따로 처리
        answer += 1
        
    for i in range(start_time, end_time): # 1초 전과 후 시침, 분침, 초침 각도 비교
        s = i * 6 % 360 # 1초 전
        m = i * 0.1 % 360
        h = i * 1/120 % 360
        # 1초 후
        ns = 360 if (i+1) * 6 % 360 == 0 else (i+1) * 6 % 360
        nm = 360 if (i+1) * 0.1 % 360 == 0 else (i+1) * 0.1 % 360
        nh = 360 if (i+1) * 1/120 % 360 == 0 else (i+1) * 1/120 % 360
        if s < m and ns >= nm: # 1초동안 초침이 분침을 역전함, 무조건 겹치는 경우
            answer += 1
        if s < h and ns >= nh:
            answer += 1
        if ns == nm == nh: # 셋 다 겹치는 경우는 한 번만 울리므로 중복 제거
            answer -= 1
    
    return answer
