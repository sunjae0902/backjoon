
def compress(s, n): # n 단위로 검사
    arr = []
    answer = ""
    for i in range(0, len(s), n):
        if arr and arr[-1][1] == s[i:i+n]:
            arr[-1][0] += 1
        else:
            arr.append([1, s[i:i+n]])
    for cnt, sub_str in arr:
        if cnt == 1:
            answer += sub_str
        else:
            answer += str(cnt) + sub_str
    return len(answer)
    
def solution(s):
    answer = 1000
    for i in range(1, 1001):
        answer = min(answer, compress(s, i))
    return answer