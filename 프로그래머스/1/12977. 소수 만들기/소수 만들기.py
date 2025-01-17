import math
def find():
    res = [2]
    for i in range(1, 1500):
        flag = 0
        for j in range(2, int(math.sqrt(2*i+1))+1):
            if (2*i+1) % j == 0:
                flag = 1
                break
        if not flag:
            res.append(2*i+1)
    return res
    
def solution(nums):
    answer = 0
    primes = find()
    combi = []

    def combinations(arr, start):
        if len(arr) == 3: # 3개를 뽑으면 끝
            combi.append(arr[:])
            return
        for i in range(start, len(nums)): # 해당하는 범위 내에서 고름
            combinations(arr + [nums[i]], i + 1) # i+1번째 수 부터 뽑기
    combinations([], 0)
    for c in combi:
        if sum(c) in primes:
            answer += 1
    return answer