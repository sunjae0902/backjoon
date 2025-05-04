def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col-1], -x[0]))
    for r in range(row_begin, row_end+1):
        tmp = 0
        for c in data[r-1]:
            tmp += c % r
        answer ^= tmp
    return answer