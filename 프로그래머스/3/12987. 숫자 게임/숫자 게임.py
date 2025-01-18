def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    a, b = 0, 0
    for i in range(len(A)):
        if B[b] > A[i]:
            a, b = a+1, b+1
            answer += 1
        else:
            B.pop()
            a += 1
    return answer