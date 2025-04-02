import sys
sys.setrecursionlimit(10**6)

def preorder(tree, node): # 루트 - 왼 - 오
    result = [node[0]]
    l_subtree=[n for n in tree if n[1] < node[1] and n[2] < node[2]]
    r_subtree=[n for n in tree if n[1] > node[1] and n[2] < node[2]]
    if l_subtree:
        result += preorder(l_subtree, l_subtree[0])
    if r_subtree:
        result += preorder(r_subtree, r_subtree[0])
    return result
    
def postorder(tree, node): # 왼 - 오 - 루트
    result = []
    l_subtree=[n for n in tree if n[1] < node[1] and n[2] < node[2]]
    r_subtree=[n for n in tree if n[1] > node[1] and n[2] < node[2]]
    if l_subtree:
        result += postorder(l_subtree, l_subtree[0])
    if r_subtree:
        result += postorder(r_subtree, r_subtree[0])
        
    result.append(node[0])
    return result 

def solution(nodeinfo):
    nodes = [(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key = lambda node: (-node[2], node[1]))
    root = nodes[0]
    return [preorder(nodes, root), postorder(nodes, root)]