def check_0(x, y, s):   # 기둥
    # 바닥 위
    if y == 0:
        return True
    # 아래에 기둥
    if (x, y-1, 0) in s:
        return True
    # 왼쪽에 보
    if (x-1, y, 1) in s:
        return True
    # 오른쪽에 보
    if (x, y, 1) in s:
        return True
    return False


def check_1(x, y, s):   # 보
    # 왼쪽 아래 기둥
    if (x, y-1, 0) in s:
        return True
    # 오른쪽 아래 기둥
    if (x+1, y-1, 0) in s:
        return True
    # 양쪽에 보
    if (x-1, y, 1) in s and (x+1, y, 1) in s:
        return True
    return False


def possible(s): 
    for x, y, a in s: # 주변만 체크하는게 아니라, 모든 구조물에 대해서 검사해야함
        if a == 0: # 종류 검사
            if not check_0(x, y, s):
                return False
        else:
            if not check_1(x, y, s):
                return False
    return True


def solution(n, build_frame):
    answer = set()   # (x, y, a)

    for x, y, a, b in build_frame:
        if b == 1:   # 설치
            answer.add((x, y, a)) # 일단 추가하고, 조건 검사 후 맞지 않으면 제거

            if not possible(answer):
                answer.remove((x, y, a))

        else:        # 삭제
            answer.remove((x, y, a)) # 일단 빼고, 조건 검사 후 맞지 않으면 다시 추가

            if not possible(answer):
                answer.add((x, y, a))

    result = list(map(list, answer)) # list로 변환
    result.sort(key=lambda x: (x[0], x[1], x[2]))
    return result