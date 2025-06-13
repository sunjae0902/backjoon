def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1) # 비트가 1개만 다른 바로 다음 수
        else:
            b = '0' + bin(n)[2:]  # 2진수 변환 함수 "0b####" 형식
            idx = b.rfind('0')   # 오른쪽에서 가장 먼저 있는 0의 위치 찾기
            b = list(b)
            b[idx] = '1' # 0->1
            b[idx + 1] = '0' # 그 옆 문자열(항상 1)을 0으로 변경
            answer.append(int(''.join(b), 2)) # 2진수를 다시 10진수로
            
    return answer