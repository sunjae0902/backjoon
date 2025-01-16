def solution(n, words):
    answer = [0,0]
    for i in range(len(words)):
        if len(words[i]) == 1 or words[i] in words[:i] or (i > 0 and words[i][0] != words[i-1][-1]):
            answer = [i % n + 1, i // n + 1]
            break
    return answer