import sys
input = sys.stdin.readline
s = input().rstrip()
# 원형 문자열에서 a를 하나로모으기, -> 양 끝에 a만 있는 경우는 괜찮음
# 원형 문자열 처리: 앞에서 필요한 만큼의 문자열을 그대로 뒤에 복사.
cnt = s.count('a')
min_cnt = len(s) - cnt
s += s[:cnt-1] # 왼쪽에 최대 cnt-1개의 문자열이 있어야 함
for i in range(len(s)-(cnt-1)):
    min_cnt = min(min_cnt, s[i:i+cnt].count('b'))
print(min_cnt)