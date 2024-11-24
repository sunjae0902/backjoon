import sys
import math
input = sys.stdin.readline

N = int(input())
dec = []
isPrime = [True] * (N+1) # 2-N
isPrime[0] = isPrime[1] = False
for i in range(2, int(math.sqrt(N))+1): # 제곱근까지만 생각해도됨
    if isPrime[i]: #i가 소수라면, i의 배수들 다 지워주기
        for j in range(i*i, N+1, i):
            isPrime[j] = False
dec = [x for x in range(len(isPrime)) if isPrime[x]]
cnt = 0
if len(dec) >= 1:          
    start, end = 0,0
    sum = dec[0]
    while start <= end:
        if sum == N:
            cnt += 1
            sum -= dec[start]
            start += 1
        elif sum < N:
            end += 1
            if end == len(dec):
                break
            sum += dec[end]
        else:
            sum -= dec[start]
            start += 1
print(cnt)