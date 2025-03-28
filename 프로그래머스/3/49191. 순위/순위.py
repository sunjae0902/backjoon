def solution(n, results):
    answer = 0
    arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for a, b in results:
        arr[a][b] = 1
        arr[b][a] = -1 
        
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if arr[j][i] == 1 and arr[i][k] == 1:
                    arr[j][k] = 1
                    arr[k][j] = -1
    for i in range(1, n+1):
        w, l = arr[i].count(1), arr[i].count(-1)
        if w + l == n-1:
            answer += 1
    return answer