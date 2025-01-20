def solution(n, left, right):
    answer = []
    # 2,3,4,5 -> 3,1,2,3 몫이 0 (나머지 0,1,2)
    for i in range(left, right+1):
        if i % n <= i // n and (i%n+1) != (i//n)%n + 1:
            answer.append((i//n)%n + 1)
        else:
            answer.append(i%n+1)
    return answer