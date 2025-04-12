def solution(cookie):
    left, right = 0, 0
    n = len(cookie)
    for m in range(n-1):
        l, r = m, m+1 # 반대 방향으로
        left_sum, right_sum = cookie[l], cookie[r]
        while l >= 0 and r < n:
            if left_sum == right_sum and (left < left_sum or right < right_sum):
                left, right = left_sum, right_sum
                continue
            if l > 0 and left_sum <= right_sum:
                l -= 1
                left_sum += cookie[l]
            elif r < n-1:
                r += 1
                right_sum += cookie[r]
            else:
                break    
    return max(left, right) if left != 0 and right != 0 else 0