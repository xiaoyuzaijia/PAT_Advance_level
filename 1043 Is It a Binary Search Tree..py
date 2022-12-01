import sys

sys.setrecursionlimit(3000)

N = int(input())
isprel = list(map(int, input().split()))
prel = []
postl = []
mprel = []
mpostl = []

class Node():
    def __init__(self, key):
        self.k = key
        self.l = None
        self.r = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.k:
            root.l = insert(root.l, key)
        else:
            root.r = insert(root.r, key)
        return root

def pre_t(root):        # 中左右
    if root is not None:
        prel.append(root.k)
        pre_t(root.l)
        pre_t(root.r)

def post_t(root):       # 左右中
    if root is not None:
        post_t(root.l)
        post_t(root.r)
        postl.append(root.k)

def mpre_t(root):       # 中右左
    if root is not None:
        mprel.append(root.k)
        mpre_t(root.r)
        mpre_t(root.l)

def mpost_t(root):      # 右左中
    if root is not None:
        mpost_t(root.r)
        mpost_t(root.l)
        mpostl.append(root.k)

if __name__ == "__main__":
    tree = None
    for i in isprel:
        tree = insert(tree, i)
    
    pre_t(tree)
    if prel == isprel:    # 是BST
        print("YES")
        post_t(tree)
        print(' '.join(list(map(str, postl))))
    else:
        mpre_t(tree)
        if mprel == isprel:   # 是镜像BST
            print("YES")
            mpost_t(tree)
            print(' '.join(list(map(str, mpostl))))
        else:                 # 都不是
            print("NO")