def solution(diffs, times, limit):
    answer = 0
    level = [i for i in range(1, max(diffs)+1)]
    s, e = 0, len(level)-1

    while s <= e:
        tmp = 0
        m = (s+e) // 2 
        for i in range(len(diffs)):
            if level[m] >= diffs[i]:
                tmp += times[i]
            else:
                tmp += (diffs[i]-level[m]) * (times[i] + times[i-1]) + times[i]
        if limit < tmp:
            s = m + 1
        else:
            e = m - 1
    answer = level[s]
    return answer