import sys
input = sys.stdin.readline
N, game = map(str, input().split())
N = int(N)
dict = {'Y':1, 'F':2, 'O': 3}
ps = set()
for i in range(N):
    p = input().rstrip()
    ps.add(p)
print(len(ps) // dict[game])