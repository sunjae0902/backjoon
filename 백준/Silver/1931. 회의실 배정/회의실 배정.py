import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*2] * N
for i in range(N):
   tmp = list(map(int, input().split()))
   arr[i] = tmp
arr.sort(key = lambda x: (x[1],x[0])) 
cnt = 0
j = 0
for i in range(N):
      if arr[i][0] >= j:
          cnt += 1
          j = arr[i][1]
      else:
          continue
print(cnt)