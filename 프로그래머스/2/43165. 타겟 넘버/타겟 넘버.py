def solution(numbers, target):
    def dfs(s, v):
        cnt = 0
        stack = [(s, v)]
        while stack:
            ind, now = stack.pop()
            if ind == len(numbers)-1:
                if now == target:
                    cnt += 1
                continue
            for x in [now+numbers[ind+1], now-numbers[ind+1]]:
                stack.append((ind+1, x))
        return cnt
    
    answer = dfs(0, numbers[0]) + dfs(0, (-1) * numbers[0])
    return answer