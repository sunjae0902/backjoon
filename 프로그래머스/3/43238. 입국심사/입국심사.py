def solution(n, times):
    answer = 0
    s, e = 0, max(times) * n
    
    while s <= e:
        finish = 0
        m = (s+e) // 2
        for time in times:
            finish += m // time
        if finish >= n:
            answer = m
            e = m -1
        else:
            s = m + 1
    return answer