import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(str, input().split()))

def combi(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combi(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result

def check(arr):
    vow = 0
    for i in range(len(arr)):
        if arr[i] in ['a', 'e', 'i', 'o', 'u']:
            vow += 1
    return True if vow > 0  and (len(arr)-vow) > 1 else False    

res = combi(arr, N)
for pwd in res:
    pwd.sort()
res.sort()
for pwd in res:
    if check(pwd):
        for i in pwd:
            print(i, end ='')
        print()