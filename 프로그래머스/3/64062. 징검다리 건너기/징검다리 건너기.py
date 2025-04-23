def solution(stones, k):
    answer = 0
    s, e = 1, max(stones)
    while s <= e:
        m = (s+e) // 2
        cnt = 0
        for i in range(len(stones)):
            if stones[i] < m:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
        if cnt >= k:
            e = m - 1
        else:
            answer = m 
            s = m + 1
    return answer