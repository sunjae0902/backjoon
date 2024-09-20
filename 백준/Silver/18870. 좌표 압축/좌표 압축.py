import sys

#sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
dict = dict()
number = list(map(int, input().split()))
for i,v in enumerate(sorted(list(set(number)))):
    dict[v] = i
for i in number:
   print(dict[i],end=' ')