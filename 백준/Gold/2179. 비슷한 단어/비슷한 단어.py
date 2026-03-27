import sys

input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

prefix_dict = dict()

# 20000 * 100 모든 접두사를 저장하는 prefix 만들기
for idx, word in enumerate(words):
    prefix = ""
    for ch in word:
        prefix += ch
        if prefix not in prefix_dict:
            prefix_dict[prefix] = [] # 초기화
        prefix_dict[prefix].append((idx, word)) # 입력 순서때문에

max_len = -1
answer = []

for prefix, words in prefix_dict.items():
    if len(words) >= 2:
        words.sort()  # index 기준 정렬

        if len(prefix) > max_len:
            max_len = len(prefix)
            answer = [words[0], words[1]]

        elif len(prefix) == max_len: # 같을 경우 입력 순서로 판단
            if words[0][0] < answer[0][0]:
                answer = [words[0], words[1]]

# 출력
(a_idx, a_word), (b_idx, b_word) = answer

if a_idx < b_idx:
    print(a_word)
    print(b_word)
else:
    print(b_word)
    print(a_word)
