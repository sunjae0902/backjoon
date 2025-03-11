def solution(prices):
    answer = [0] * len(prices)
    n = len(prices)
    for i in range(n):
        for j in range(i+1, n):
            if prices[j] < prices[i]:
                answer[i] = j-i
                break
            else:
                answer[i] += 1
    return answer