import sys
input = sys.stdin.readline
st = list(input().rstrip())
M = int(input())
point = len(st)
popped = []
for i in range(M):
    tmp = list(map(str, input().split()))
    if tmp[0] == 'L' and len(st) > 0:
        popped.append(st.pop())
    elif tmp[0] == 'B' and len(st) > 0:
        st.pop()
    elif tmp[0] == 'D' and len(popped) > 0:
        st.append(popped.pop())
    elif tmp[0] == 'P':
        st.append(tmp[1])
for i in st:
    print(i, end='')
for i in popped[::-1]:
    print(i, end='')