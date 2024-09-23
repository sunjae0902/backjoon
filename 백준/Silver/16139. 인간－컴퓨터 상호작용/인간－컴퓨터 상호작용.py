import sys
input = sys.stdin.readline

s = input().strip()  # 문자열 끝 공백 제거
q = int(input())     # 쿼리 수 입력

cnt = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(len(s)):
    c = ord(s[i]) - 97  # 현재 문자의 알파벳 인덱스 (0 ~ 25)
    cnt[i+1] = cnt[i][:]
    cnt[i+1][c] += 1 # 갱신

for _ in range(q):
    a, l, r = input().split()
    a = ord(a) - 97  # 알파벳을 숫자로 변환
    l = int(l)
    r = int(r)

    # r까지의 누적합에서 l-1까지의 누적합을 빼기
    print(cnt[r+1][a] - cnt[l][a])