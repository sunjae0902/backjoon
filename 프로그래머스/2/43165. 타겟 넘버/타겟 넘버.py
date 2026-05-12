def solution(numbers, target):
    answer = 0
    combis = []
    def dfs(cur):
        depth = len(cur)
        if depth == len(numbers):
            combis.append(cur)
            return
        dfs(cur + "+")
        dfs(cur + "-")
    dfs('')
    for combi in combis:
        res = 0
        for i in range(len(numbers)):
            if combi[i] == '+':
                res += numbers[i]
            else:
                res -= numbers[i]
        if res == target:
            answer += 1
    return answer