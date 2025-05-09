def dist(x, y):
    return (x[0]-y[0]) ** 2 + (x[1]-y[1]) ** 2

def solution(m, n, startX, startY, balls):
    answer = []
    start = (startX, startY)
    for x, y in balls:
        reverse = [(-x, y), (2*m-x, y), (x, -y), (x, 2*n-y)]
        min_dist = int(1e9)
        for rx, ry in reverse:
            if rx == x == startX and ((startY < y < ry) or (ry < y < startY)):
                continue
            if ry == y == startY and ((startX < x < rx) or (rx < x < startX)):
                continue
            min_dist = min(min_dist, dist(start, (rx, ry)))
        answer.append(min_dist)
    return answer