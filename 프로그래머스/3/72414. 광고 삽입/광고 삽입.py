def to_sec(time):
    return 60 * 60 * int(time[:2]) + 60 * int(time[3:5]) + int(time[6:])

def to_str(sec):
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    return f"{h:02d}:"+f"{m:02d}:"+f"{s:02d}"

def solution(play_time, adv_time, logs):
    answer = ''
    play_sec = to_sec(play_time)
    adv_sec = to_sec(adv_time)
    count = [0] * (play_sec + 1) # i초~i+1초
    
    for log in logs:
        tmp = log.split('-')
        s, e = to_sec(tmp[0]), to_sec(tmp[1])
        count[s] += 1
        count[e] -= 1 
        
    for i in range(1, play_sec): # 카운트를 모두 표시하기 위한 누적합
        count[i] += count[i-1]
        
    for i in range(1, play_sec): # 카운트를 합산하기 위한 누적합
        count[i] += count[i-1]
        
    max_time = 0
    for start in range(play_sec - adv_sec + 1):
        end = start + adv_sec - 1
        total = count[end] - (count[start-1] if start > 0 else 0)
        if max_time < total:
            max_time = total
            answer = to_str(start)
        
    return answer