def solution(distance, rocks, n):
    answer = 0
    s, e = 1, distance # 가능한 사이 거리 중 최댓값
    rocks.sort()
    rocks.append(distance)
    
    while s <= e:
        m = (s+e) // 2
        delete = 0
        prev_rock = 0
        for rock in rocks:
            dist = rock - prev_rock
            if dist < m:
                delete += 1
                # 제거한 바위가 너무 많다면 break
                if delete > n:
                    break
            # 바위를 제거하지 않았다면, prev_rock을 갱신
            else:
                prev_rock = rock
        if delete > n:
            e = m - 1
        else:
            answer = m
            s = m + 1
    return answer