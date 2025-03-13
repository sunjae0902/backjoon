def solution(people, limit):
    answer = 0
    stack = []
    people.sort(reverse = True)
    for w in people:
        if stack and stack[-1] + w <= limit:
            stack.pop()
            answer += 1
            continue
        stack.append(w)
    answer += len(stack)
    return answer