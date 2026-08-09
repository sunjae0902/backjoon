def minute(s):
    return int(s[:2]) * 60 + int(s[3:])
def parse(m):
    arr = []
    ind = 0
    while ind < len(m):
        if ind+1 < len(m) and m[ind+1] == '#':
            arr.append(m[ind:ind+2])
            ind += 2
        else:
            arr.append(m[ind])
            ind += 1
    return arr

def contains(arr1, arr2):
    for i in range(len(arr1)-len(arr2)+1):
        if arr2 == arr1[i:i+len(arr2)]:
            return True
    return False
    
def solution(m, musicinfos):
    musicinfos = [st.split(",") for st in musicinfos]
    candidates = []
    
    for i in range(len(musicinfos)):
        s, e, t, melody = musicinfos[i]
        dur = minute(e) - minute(s)
        total = []
        melody_arr = parse(melody)
        for j in range(dur):
            total.append(melody_arr[j % len(melody_arr)])
            
        if contains(total, parse(m)):
            candidates.append((dur, i, t))
        candidates.sort(key = lambda x: (-x[0], x[1]))
        
    if not candidates:
        return "(None)"
    return candidates[0][-1]