import sys
input = sys.stdin.readline

N = int(input())
s = set()
for i in range(N):
    tmp = list(map(str,input().split()))
    if len(tmp) == 1:
        if tmp[0] == "all":
            s = set(i for i in range(1, 21))
        elif tmp[0] == "empty":
            s = set()
    else:
        cmd, x = tmp[0], int(tmp[1])
        if cmd == "add":
            s.add(x)
        elif cmd == "remove" and x in s:
            s.remove(x)
        elif cmd == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)
        elif cmd == "check":
            print("1" if x in s else "0")