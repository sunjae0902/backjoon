import math

def solution(arrayA, arrayB):
    answer = []
    arrayA, arrayB = list(set(arrayA)), list(set(arrayB))
    # a의 최대공약수 && !b의 공약수
    # b의 최대공약수 && !a의 공약수
    possible = [arrayA[0], arrayB[0]]
    for a in arrayA[1:]:
        possible[0] = math.gcd(possible[0], a)
    for b in arrayB[1:]:
        possible[1] = math.gcd(possible[1], b)
        
    for a in arrayA:
        if a % possible[1] == 0:
            break
    else:
        answer.append(possible[1])
    for b in arrayB:
        if b % possible[0] == 0:
            break
    else:
        answer.append(possible[0])
    return max(answer) if answer != [] else 0