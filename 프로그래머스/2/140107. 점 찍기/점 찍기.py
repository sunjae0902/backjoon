def solution(k, d):
    import math
    count = 0
    for x in range(0, d + 1, k):
        max_y = int((d ** 2 - x ** 2) ** 0.5)
        count += (max_y // k) + 1  # y = 0 도 포함되므로 +1
    return count
