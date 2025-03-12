def solution(n):
    answer = []
    
    def hanoi(s, e, n):
        m = [i for i in [1,2,3] if i not in [s,e]][0]
        if n == 1:
            answer.append([s,e])
            return
        hanoi(s, m, n-1)
        hanoi(s, e, 1)
        hanoi(m, e, n-1)
        
    hanoi(1,3,n)
    return answer