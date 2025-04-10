def solution(n):
    def dfs(open_cnt, close_cnt): #열린, 닫힌
        if open_cnt == n and close_cnt == n:
            return 1
        count = 0
        if open_cnt < n:
            count += dfs(open_cnt + 1, close_cnt)
        if close_cnt < open_cnt:
            count += dfs(open_cnt, close_cnt + 1)
        return count

    return dfs(0, 0)
