def solution(n):
    answer = 0
    stack = [[0,0]]
    while stack:
        o, c = stack.pop()
        if o == n and c == n:
            answer += 1
        if o < n:
            stack.append([o+1, c])
        if c < o:
            stack.append([o, c+1])
    return answer