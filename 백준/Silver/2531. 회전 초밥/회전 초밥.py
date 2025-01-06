import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi += sushi[:k-1]
ans = []
for i in range(len(sushi)-(k-1)):
    s = set(sushi[i:i+k])
    s.add(c)
    ans.append(len(s))
print(max(ans))