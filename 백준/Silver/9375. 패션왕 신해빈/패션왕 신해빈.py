import sys
input = sys.stdin.readline

T = int(input())

def solve():
    dict = {}
    N = int(input())
    for _ in range(N):
        v, k = map(str,input().split())
        if k not in dict:
            dict[k] = []  # 빈 리스트로 초기화
        dict[k].append(v)  # 리스트에 값 추가
        
    res = 1
    for key in dict.keys():
        res *= (len(dict.get(key)) + 1)
    print(res-1)
        
for i in range(T):
    solve()