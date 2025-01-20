def solution(numbers):
    answer = sum([i for i in range(1, 10) if i not in numbers])
    return answer