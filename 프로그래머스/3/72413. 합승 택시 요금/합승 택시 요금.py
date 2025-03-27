def solution(n, s, a, b, fares):
    answer = int(1e9)
    arr = [[int(1e9) for _ in range(1+n)] for _ in range(1+n)]
    
    for i in range(1, n+1):
        arr[i][i] = 0
        
    for start, end, weight in fares:
        arr[start][end] = weight
        arr[end][start] = weight
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if j == k:
                    continue
                if arr[j][i] + arr[i][k] < arr[j][k]:
                    arr[j][k] = arr[j][i] + arr[i][k]
                    
    for i in range(1, n+1): # i번 노드까지 합승
        together = arr[s][i] + arr[i][a] + arr[i][b]
        answer = min(answer, together)
        
    return answer