def integer(arr):
    return arr[0].is_integer() and arr[1].is_integer()

def sol_equation(line1, line2):
    a1, b1, c1 = line1
    a2, b2, c2 = line2

    if a1 * b2 == a2 * b1:
        return []

    x_numerator = b1 * c2 - b2 * c1 
    x_denominator = a1 * b2 - a2 * b1
    x = x_numerator / x_denominator

    if b1 != 0:
        y = (-c1 - a1 * x) / b1
    else:
        y = (-c2 - a2 * x) / b2

    if integer([x, y]):
        return [int(x), int(y)]
    return []

def solution(line):
    int_crosses = set()
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            cross = sol_equation(line[i], line[j])
            if cross:
                int_crosses.add(tuple(cross))

    if not int_crosses:
        return []

    max_x = max(x for x, y in int_crosses)
    min_x = min(x for x, y in int_crosses)
    max_y = max(y for x, y in int_crosses)
    min_y = min(y for x, y in int_crosses)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    answer = [['.' for _ in range(width)] for _ in range(height)]

    for x, y in int_crosses:
        row = max_y - y       # y 좌표: 위->아래
        col = x - min_x       # x 좌표: 왼->오
        answer[row][col] = '*'

    return [''.join(row) for row in answer]  # 문자열 리스트로 반환
