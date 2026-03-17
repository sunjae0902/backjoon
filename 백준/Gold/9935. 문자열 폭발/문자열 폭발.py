import sys
input = sys.stdin.readline

origin = input().strip()
explosion = input().strip()
e = len(explosion)

st = []

for s in origin:
    st.append(s)
    if len(st) >= e and ''.join(st[-e:]) == explosion:
        for _ in range(e):
            st.pop()

result = ''.join(st)
print(result if len(result) != 0 else "FRULA")