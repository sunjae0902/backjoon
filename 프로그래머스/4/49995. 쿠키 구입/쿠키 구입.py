def solution(cookie):
    cookies = [0,0]
    n = len(cookie)
    for m in range(n-1):
        left, right = m, m+1
        left_sum, right_sum = cookie[m], cookie[m+1]
        while left >= 0 and right < n:
            if left_sum == right_sum and (left_sum > cookies[0] or right_sum > cookies[1]):
                cookies = [left_sum, right_sum]
                continue
            if left_sum <= right_sum and left > 0:
                left -= 1
                left_sum += cookie[left]
            elif right < n-1:
                right += 1
                right_sum += cookie[right]
            else:
                break
    return max(cookies) if all(c for c in cookies) else 0