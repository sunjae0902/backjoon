def solution(sequence, k):
    answer = []
    s, e, min_len = 0,0, int(1e6)
    sub = sequence[0]
    while e < len(sequence):
        if sub == k:
            answer.append([s,e])
            sub -= sequence[s]
            s += 1
        elif sub > k:
            sub -= sequence[s]
            s += 1
        else:
            e += 1
            if e < len(sequence):
                sub += sequence[e]
            
    answer.sort(key = lambda x: (x[1]-x[0], x[0]))
    return answer[0]