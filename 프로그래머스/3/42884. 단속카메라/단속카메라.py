def get_overlap_coor(c1, c2):
    if c1[1] < c2[0] or c2[1] < c1[0]: 
        return []
    return [max(c1[0], c2[0]), min(c1[1], c2[1])] 

def solution(routes):
    camera = []
    routes.sort()
    for route in routes:
        if not camera:
            camera.append(route)
            continue
        flag = 0
        for i in range(len(camera)):
            coor = get_overlap_coor(camera[i], route)
            if coor:
                flag = 1
                camera[i] = coor
                break
        if not flag:
            camera.append(route)

    return len(camera)