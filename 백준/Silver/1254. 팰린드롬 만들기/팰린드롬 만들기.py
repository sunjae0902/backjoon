import sys
input = sys.stdin.readline
st = input().rstrip()

def is_palindrome(s):
    return s == s[::-1]
for i in range(len(st)):
    if is_palindrome(st[i:]):
        print(len(st) + i)
        break