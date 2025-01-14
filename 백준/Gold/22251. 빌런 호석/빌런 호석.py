import sys
input = sys.stdin.readline
n, k, p, x = map(int,input().split())
arr = [[0 for _ in range(10)] for _ in range(10)]
led = [[1,1,1,0,1,1,1],
       [0,0,0,0,0,1,1],
       [0,1,1,1,1,1,0],
       [0,0,1,1,1,1,1],
       [1,0,0,1,0,1,1],
       [1,0,1,1,1,0,1],
       [1,1,1,1,1,0,1],
       [0,0,1,0,0,1,1],
       [1,1,1,1,1,1,1],
       [1,0,1,1,1,1,1]]

num = []
for i in range(10): # XOR 연산 후 1의 개수로도 구하기 가능
    count = [0] * 10
    for j in range(10):
        if i != j:
            for m in range(7):
                if led[i][m] != led[j][m]:
                    count[j] += 1
    num.append(count)

def dfs(s, arr):
    stack = [(s, p, arr)] # 깊이, 남은 가능한 개수, 바꾸려는 숫자 배열
    result = 0
    while stack:
        pos, remain_p, curr_arr = stack.pop()
        if pos == k: # 끝까지 순회한 후
            changed = int("".join(map(str, curr_arr)))
            if 1 <= changed <= n and changed != x: # 유효성 검사
                result += 1
            continue
        
        curr_digit = curr_arr[pos] # 바꾸려는 숫자
        for i, v in enumerate(num[curr_digit]):
            if v <= remain_p: # remain_p 이하만 가능
                new_arr = curr_arr.copy()
                new_arr[pos] = i # 바꿈 
                stack.append((pos + 1, remain_p - v, new_arr))

    return result

ind = k
q = x
floor = []
while ind > 0:
    ind -= 1
    floor.append(q // (10**ind))
    q %= (10**ind)
print(dfs(0, floor))