import sys
sys.setrecursionlimit(10**6)

def find_subtree(tree, node):
    left = [n for n in tree if n[1] < node[1] and n[2] < node[2]]
    right = [n for n in tree if n[1] > node[1] and n[2] < node[2]]
    return left, right

def preorder(tree, node): # 루트 - 왼 - 오
    result = [node[0]]
    left, right = find_subtree(tree, node)
    if left:
        result += preorder(left, left[0])
    if right:
        result += preorder(right, right[0])
    return result
    
def postorder(tree, node): # 왼 - 오 - 루트
    result = []
    left, right = find_subtree(tree, node)
    if left:
        result += postorder(left, left[0])
    if right:
        result += postorder(right, right[0])
    result += [node[0]]
    return result 

def solution(nodeinfo):
    nodes = [(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key = lambda node: (-node[2], node[1]))
    root = nodes[0]
    return [preorder(nodes, root), postorder(nodes, root)]