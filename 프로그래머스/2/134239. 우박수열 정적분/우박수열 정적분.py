def solution(k, ranges):
    answer = []
    data = [0, k]

    while k != 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = 3 * k + 1
        data.append(k)

    n = len(data) - 1 
    
    for i in range(1, n):
        data[i] = data[i-1] + (data[i] + data[i+1]) / 2

    for s, e in ranges:
        e += n-1
        if s > e:
            answer.append(-1)
        else:
            answer.append(data[e]-data[s])
    return answer