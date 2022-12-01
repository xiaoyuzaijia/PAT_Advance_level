N = int(input())

class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    

def get_levell(root):
    levell = []
    q = [root]
    
    while q:
        node = q.pop(0)
        levell.append(node.key)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return levell

def build_tree(postl, inl):   #通过后序和中序建立树
    if not postl:
        root = None
    else:
        root = Node(postl[-1])
        root_idx = inl.index(root.key)

        left_postl = postl[:root_idx]
        left_inl = inl[:root_idx]
        left = build_tree(left_postl, left_inl)

        right_postl = postl[root_idx:-1]
        right_inl = inl[root_idx+1:]
        right = build_tree(right_postl, right_inl)

        root.left = left
        root.right = right

    return root

if __name__ == "__main__":
    postl = input().split()
    inl= input().split()
    
    mytree = build_tree(postl, inl)
    levell = get_levell(mytree)
    
    print(' '.join(levell))