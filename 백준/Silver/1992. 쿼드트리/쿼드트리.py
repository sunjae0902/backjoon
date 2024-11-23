import sys
input = sys.stdin.readline
N = int(input())
arr = []
arr = [list(map(int, input().rstrip())) for _ in range (N)]

def recur(x,y,n): # 0,0,4
    value = arr[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != value:
                print("(", end = '')
                for m in range(2): # 달라지면 4개로 쪼개서 비교
                    for k in range(2):
                        recur(x+ m * n // 2, y + k * n // 2, n // 2)
                print(")", end = '')  
                return      
    print(value, end = '')
      
recur(0,0, N)