import sys, queue
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = queue.Queue()
    for i in range(len(arr)):
        q.put(i)  
    res = []
    while not q.empty():
        a = q.get()
        remain = list(q.queue)
        flag = 0
        for i in range(len(remain)):
            if arr[a] < arr[remain[i]]:
                q.put(a)
                flag = 1
                break
        if flag == 0:
            res.append(a)

    for i in range(len(res)):
        if res[i] == M:
            print(i+1)
            break