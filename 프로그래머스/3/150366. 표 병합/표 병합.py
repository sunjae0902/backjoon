def solution(commands):
    # 대표 셀
    parent = [[(i, j) for j in range(50)] for i in range(50)]
    # 대표 셀 값 기록
    value = dict()
    
    def find(r, c):
        if parent[r][c] != (r, c):
            parent[r][c] = find(*parent[r][c]) # 튜플 언패킹
        return parent[r][c]
    
    def union(r1, c1, r2, c2):
        p1 = find(r1, c1)
        p2 = find(r2, c2)
        
        if p1 == p2:
            return
        
        v1 = value.get(p1, "")
        v2 = value.get(p2, "")
        
        # p2를 p1 밑으로
        parent[p2[0]][p2[1]] = p1
        
        if v1 == "" and v2 != "":
            value[p1] = v2
        elif v1 != "":
            value[p1] = v1
        
        if p2 in value:
            del value[p2]
    
    def update_cell(r, c, val):
        p = find(r, c)
        value[p] = val
    
    def update_all(v1, v2):
        for k in list(value.keys()):
            if value[k] == v1:
                value[k] = v2
    
    def unmerge(r, c):
        p = find(r, c)
        keep = value.get(p, "")
        
        cells = []
        for i in range(50):
            for j in range(50):
                if find(i, j) == p:
                    cells.append((i, j))
        
        for i, j in cells:
            parent[i][j] = (i, j)
        
        if p in value:
            del value[p]
        
        if keep != "":
            value[(r, c)] = keep
    
    answer = []
    
    for cmd in commands:
        cmd = cmd.split()
        
        if cmd[0] == "UPDATE":
            if len(cmd) == 4:
                r, c, val = int(cmd[1])-1, int(cmd[2])-1, cmd[3]
                update_cell(r, c, val)
            else:
                v1, v2 = cmd[1], cmd[2]
                update_all(v1, v2)
        
        elif cmd[0] == "MERGE":
            r1, c1, r2, c2 = map(lambda x: int(x)-1, cmd[1:])
            union(r1, c1, r2, c2)
        
        elif cmd[0] == "UNMERGE":
            r, c = int(cmd[1])-1, int(cmd[2])-1
            unmerge(r, c)
        
        elif cmd[0] == "PRINT":
            r, c = int(cmd[1])-1, int(cmd[2])-1
            p = find(r, c)
            answer.append(value.get(p, "EMPTY"))
    
    return answer