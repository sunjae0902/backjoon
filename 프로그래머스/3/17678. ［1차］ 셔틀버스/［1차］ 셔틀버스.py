def tomin(s):
    return 60 * int(s[0:2]) + int(s[3:])

def tostr(m):
    return f'{m//60:02d}:{m%60:02d}'

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort(key = lambda x: tomin(x))
    arrival = 60 * 9
    time, idx = 0, 0
    
    for i in range(n): #n번 반복 
        people = 0
        while people < m and idx < len(timetable) and arrival >= tomin(timetable[idx]):
            time = tomin(timetable[idx])
            idx += 1
            people += 1
        if i == n-1: # 마지막 버스
            if people < m:
                answer = tostr(arrival)
            else:
                answer = tostr(time-1)
        arrival += t
    return answer