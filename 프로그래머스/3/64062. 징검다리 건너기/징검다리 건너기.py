def solution(stones, k):
    left, right = 1, max(stones) # 최대 건널 수 있는 사람 수
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        max_cnt = 0
        
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0

        if cnt >= k:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer
