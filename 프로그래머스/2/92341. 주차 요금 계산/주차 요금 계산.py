from collections import defaultdict
import math

def get_duration(start, end):
    start_h, start_m = int(start[:2]) * 60, int(start[3:])
    end_h, end_m = int(end[:2]) * 60, int(end[3:])
    return end_h + end_m - start_h - start_m
    
def solution(fees, records):
    answer = []
    times = defaultdict(int)
    cars = defaultdict(str)
    
    for record in records:
        t, n, flag = list(record.split())
        if flag == 'IN':
            cars[n] = t
        else:
            times[n] += get_duration(cars[n], t)
            cars[n] = ''
            
    # 남은 시간 처리, 23:59 출차
    for n, t in cars.items():
        if t != '':
            times[n] += get_duration(t, "23:59")
            
    answer = sorted([[n, t] for n, t in times.items()], key = lambda x: x[0])
    for i in range(len(answer)):
        fee = fees[1]
        if answer[i][1] > fees[0]:
            unit_time_fee = math.ceil((answer[i][1] - fees[0]) / fees[2])
            fee += unit_time_fee * fees[3]
        answer[i] = fee
    return answer