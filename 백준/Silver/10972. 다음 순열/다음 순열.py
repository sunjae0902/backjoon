import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 아이디어: 이전 수열 -> 다음 수열로 갈 때, 점점 오름차순 -> 내림차순 수열로 감
# 마지막 원소부터 검사하면서, 비교 (arr[i-1],arr[i]) 원소가 감소하는 순간 (오름 차순이 깨지는 순간) 
# 감소한 수 (arr[i-1]) 보다 가장 근소하게 큰 수를 구한다(사전순)
# 둘이 swap 후 오름차순 정렬 (왜? swap 한 후 가장 처음의 다음 순열이 오도록, 즉 사전순으로 배열하기 위해.)
# 정렬된 arr[i:]와 arr[:i]를 붙이면 끝

flag = 0

for i in range(N-1, 0, -1):
    if flag:
        break
    if arr[i] > arr[i-1]:
        for j in range(N-1, 0, -1):
            if arr[i-1] < arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:])
                flag = 1
                break
            
if flag == 0:
    print("-1")
else:
    for i in arr:
        print(i, end = ' ')