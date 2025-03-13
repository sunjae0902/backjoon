def solution(sizes):
    for w in range(1, 1001):
        for h in range(1, 1001):
            if all((size[0] <= h and size[1] <= w) or (size[0] <= w and size[1] <= h) for size in sizes):
                return w * h