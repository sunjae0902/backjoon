def solution(numbers): # 문자열 정렬 
    answer = sorted([str(i) for i in numbers], key = lambda x : x*3, reverse = True)
    answer = ''.join(answer) 
    return answer if len(answer) != answer.count('0') else '0'