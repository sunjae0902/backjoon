users = set()
sum = 0

N = int(input())
for i in range(0,N):
  name = input()
  if(name == "ENTER"):
    sum += len(users)
    users = set()
    continue
  else:
    users.add(name)
sum += len(users)

print(sum)