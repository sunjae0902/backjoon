def solution(n, times):
    answer = 0
    s, e = 1, max(times) * n

    while s <= e:
        people = 0
        m = (s+e) // 2
        for time in times:
            people += m // time
            if people >= n:
                break
        if people >= n:
            answer = m
            e = m - 1
        else:
            s = m + 1
    return answer