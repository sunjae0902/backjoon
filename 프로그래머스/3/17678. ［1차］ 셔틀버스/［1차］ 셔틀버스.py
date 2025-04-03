def to_string(m):
    return f'{m // 60:02d}:{m % 60:02d}' # 형식 지정 문자열

def to_min(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def solution(n, t, m, timetable):
    timetable = sorted(to_min(time) for time in timetable)
    
    bus_time = 60 * 9 # 시작
    last_arrival = 0
    idx = 0
    
    for i in range(n): # n번 반복 
        # 현재 버스에 탈 수 있는 최대 인원 계산
        count = 0
        while idx < len(timetable) and timetable[idx] <= bus_time and count < m:
            last_arrival = timetable[idx]
            count += 1
            idx += 1
        
        # 마지막 버스
        if i == n - 1:
            if count < m:
                return to_string(bus_time)
            else:
                # 자리가 없다면 마지막으로 탄 사람보다 1분 먼저 와야 함
                return to_string(last_arrival - 1)

        bus_time += t

    return to_string(bus_time)
