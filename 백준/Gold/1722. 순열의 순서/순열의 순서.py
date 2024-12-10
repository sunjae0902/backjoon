import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n - 1) * n


def recur(arr, parr, n, k): # parr[1,2,3, .. , N]
    if n == 1:
        return arr + parr # 마지막 남은 한 개 더해서 반환
    block_size = fact(n - 1) # 첫 자리를 고정했을 때 각 단계마다 (n-1)!개의 수열 생성됨
    a = (k - 1) // block_size  # 첫째 자리에 따라 그룹화해서 구하고자 하는 수열의 인덱스 계산
    newItem = parr[a] # 더할 아이템
    parr.pop(a) # 빼주기.
    new_k = k - a * block_size # 몇개 더해졌는지 업데이트
    return recur(arr + [newItem], parr, n - 1, new_k)


if arr[0] == 1:
    k = arr[1]
    res = recur([],[i for i in range(1, N+1)], N, k)
    for i in res:
        print(i, end = ' ')

elif arr[0] == 2:
    cnt = 0 
    target = arr[1:]
    visited = []
    for i in range(len(target)):
        c = sum(1 for j in range(1, target[i]) if j not in visited)
        cnt += fact(N-i-1) * c
        visited.append(target[i])
    print(cnt+1)
