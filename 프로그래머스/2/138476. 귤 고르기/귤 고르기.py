from collections import Counter
def solution(k, tangerine):
    answer = 0
    n = len(set(tangerine))
    d = sorted(Counter(tangerine).items(), key = lambda x: x[1], reverse = True)

    for i in range(len(d)):
        t, cnt = d[i]
        if cnt > 0:
            d[i] = (t, max(cnt-k, 0))
            k -= cnt
            answer += 1
            if k <= 0:
                break
    return answer