def solution(n, times):
    answer = 0
    s, e = 1, max(times) * n
    while s <= e:
        m = (s + e) // 2
        people = 0
        for time in times:
            people += m // time # 각 심사대에서 동시에 심사할 수 있는 사람 수 
            if people > n:
                break
        if people >= n:
            answer = m
            e = m - 1
        else:
            s = m + 1
    return answer