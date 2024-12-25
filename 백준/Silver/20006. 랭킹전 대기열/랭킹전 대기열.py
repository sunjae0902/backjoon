import sys
input = sys.stdin.readline
p, m = map(int, input().split())
rooms = []

for i in range(p):
    level, name = map(str, input().split())
    level = int(level)
    if len(rooms) < 1:
        rooms.append([[level, name]])
        continue
    flag = 0
    for room in rooms:
        if len(room) < m:
            if room[0][0] - 10 <= level <= room[0][0] + 10:
                room.append([level, name])
                flag = 1
                break
    if not flag:
        rooms.append([[level, name]])
       
for room in rooms:
    print("Started!" if len(room) == m else "Waiting!")
    room.sort(key = lambda x: x[1])
    for r in room:
        print(r[0], r[1])