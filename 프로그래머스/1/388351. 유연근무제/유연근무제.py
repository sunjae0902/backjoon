def convert(time):
    h = time // 100
    m = time % (h*100)
    return 60*h + m

def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    for i in range(n):
        end = convert(schedules[i]+10)
        flag = 1
        for j in range(7):
            day = startday + j if startday+j < 8 else (startday+j) % 8 + 1
            if day < 6 and convert(timelogs[i][j]) > end:
                flag = 0
        if flag:
            answer += 1
    return answer