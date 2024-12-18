import sys
input = sys.stdin.readline
vow = ['a','e','i','o','u']
while True:
    pwd = input().rstrip()
    if pwd == "end":
        break
    flag = [0,1,1]
    for s in pwd:
        if s in vow:
            flag[0] = 1
            break
    if len(pwd) >= 2:
        for i in range(0, len(pwd)-1):
            if pwd[i] == pwd[i+1]:
                if pwd[i] == 'e' or pwd[i] == 'o':
                    flag[1] = 1
                else:
                    flag[1] = 0
                    break
    if len(pwd) >= 3:
        for i in range(0, len(pwd)-2):
            if (pwd[i] in vow and pwd[i+1] in vow and pwd[i+2] in vow) or (pwd[i] not in vow and pwd[i+1] not in vow and pwd[i+2] not in vow):
                flag[2] = 0
                break
            else:
                flag[2] = 1
    if flag == [1,1,1]:
        print("<" + pwd + "> is acceptable.")
    else:
        print("<" + pwd + "> is not acceptable.")