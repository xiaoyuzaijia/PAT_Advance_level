N = int(input())
insertl = list(map(int, input().split()))

class Node():
    def __init__(self, k=None, l=None, r=None):
        self.k = k
        self.l = l
        self.r = r

def insert(root, k):
    if root is None:
        root = Node(k)
    
    elif k < root.k:
        root.l = insert(root.l, k)
        if get_h(root.l) - get_h(root.r) > 1:
            if k < root.l.k:
                root = ll_r(root)
            else:
                root.l = rr_r(root.l)
                root = ll_r(root)
    else:
        root.r = insert(root.r, k)
        if get_h(root.l) - get_h(root.r) < -1:
            if k > root.r.k:
                root = rr_r(root)
            else:
                root.r = ll_r(root.r)
                root = rr_r(root)
    
    return root



def get_h(root):
    if not root:
        return 0
    return max(get_h(root.l), get_h(root.r)) + 1

def ll_r(root):
    n_root = root.l
    root.l = n_root.r
    n_root.r = root
    return n_root

def rr_r(root):
    n_root = root.r
    root.r = n_root.l
    n_root.l = root
    return n_root

if __name__ == "__main__":
    my_AVL = None
    for i in insertl:
        my_AVL = insert(my_AVL, i)
    
    print(my_AVL.k, end='')