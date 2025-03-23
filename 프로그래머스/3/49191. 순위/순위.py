def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = -1
        
    # 플로이드-워셜 
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1  # i가 j를 이김
                    graph[j][i] = -1 # j가 i에게 짐
    answer = 0
    for i in range(1, n + 1):
        count = sum(1 for j in range(1, n + 1) if graph[i][j] != 0)
        if count == n - 1: # 이긴 + 진 수가 n-1이면 확정 가능
            answer += 1
    return answer
