import math

def solution(begin, end):
    answer = []

    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue

        block = 1

        for d in range(2, int(math.sqrt(num)) + 1):
            if num % d == 0:
                # 큰 약수가 1천만 이하라면 그것이 정답
                if num // d <= 10000000:
                    block = num // d
                    break
                # 아니면 작은 약수를 후보로 저장
                block = d

        answer.append(block)

    return answer