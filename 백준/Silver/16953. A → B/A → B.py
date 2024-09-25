import sys
input = sys.stdin.readline

a,b = map(int, input().split())
cnt = 0
while True:
    if a == b:
        break
    elif b % 2 != 0 and b % 10 != 1 or a > b:
        cnt = -2
        break
    elif str(b)[-1] == '1':
        b = int(str(b)[:-1])
        cnt += 1
    else:
        b //= 2
        cnt += 1
print(cnt+1)