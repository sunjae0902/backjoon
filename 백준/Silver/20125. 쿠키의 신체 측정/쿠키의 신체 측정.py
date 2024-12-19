import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
cookie = [0, 0, 0, 0, 0, 0, 0] # hr, hc, la, ra, w, ll, rl
for i in range(N):
    s = input()
    for j in range(len(s)):
        if s[j] == '*':
            if cookie == [0] * 7 :
                cookie[0], cookie[1] = i+2, j+1
                continue
            if i == cookie[0]-1:
                if j < cookie[1]-1:
                    cookie[2] += 1
                elif j > cookie[1]-1:
                    cookie[3] += 1
                continue
            if i > cookie[0]-1:
                if j == cookie[1]-1:
                    cookie[4] += 1
                else:
                    if j < cookie[1]-1:
                        cookie[5] += 1
                    elif j > cookie[1]-1:
                        cookie[6] += 1  
                continue              
print(cookie[0], cookie[1])
for i in cookie[2:]:
    print(i, end = ' ')