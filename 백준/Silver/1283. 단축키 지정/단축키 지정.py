import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
keys = []
for i, words in enumerate(arr):
    flag = 0
    for j, word in enumerate(words):
        if word[0].lower() not in keys:
            keys.append(word[0].lower())
            arr[i][j] = "[" + word[0] + "]" + word[1:]
            flag = 1
            break
    if not flag:
        for j, word in enumerate(words):
            for k in range(1, len(word)):
                if not flag and word[k].lower() not in keys:
                    keys.append(word[k].lower())
                    arr[i][j] = word[:k]+ "[" + word[k] + "]" + word[k+1:]
                    flag = 1
                    break
    for word in words:
        print(word, end=' ')
    print()