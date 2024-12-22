import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

if max(arr) == 0:
    print("SAD")
else:
    prefix = [0]
    prefix.append(arr[0])
    for i in range(2, len(arr)+1):
        prefix.append(prefix[i-1] + arr[i-1])
    max_cnt = 0
    cnt = 1
    for i in range(len(prefix)-X):
        if max_cnt <= prefix[i+X] - prefix[i]:
            if max_cnt == prefix[i+X]-prefix[i]:
                cnt += 1
            else:
                max_cnt = prefix[i + X] - prefix[i]  
                cnt = 1
    print(max_cnt)
    print(cnt)