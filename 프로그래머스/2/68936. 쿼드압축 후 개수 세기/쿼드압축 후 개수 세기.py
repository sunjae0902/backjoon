def solution(arr):
    answer = [0,0]
    
    def recur(x, y, size):
        val = arr[x][y]
        if size == 1:
            answer[val] += 1
            return
        
        if all(arr[i][j] == val for i in range(x, x+size) for j in range(y, y+size)):
            answer[val] += 1
        else:
            recur(x, y, size//2)
            recur(x, y+size//2, size//2)
            recur(x+size//2, y, size//2)
            recur(x+size//2, y+size//2, size//2)
    
            
    recur(0, 0, len(arr))
    return answer