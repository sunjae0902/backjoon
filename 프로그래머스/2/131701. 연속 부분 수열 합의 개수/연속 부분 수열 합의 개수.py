def solution(elements):
    answer = []
    n = len(elements)
    for i in range(1, n+1):
        for j in range(n):
            if j+i < n+1:
                answer.append(sum(elements[j:j+i]))
            else:
                answer.append(sum(elements[j:]) + sum(elements[:(i+j)%n]))
    return len(set(answer))