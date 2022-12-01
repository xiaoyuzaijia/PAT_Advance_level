N = int(input())
prel = []
inl = []

def get_posl(prel, inl):
    if not prel:
        return []
    root = prel[0]
    i = inl.index(root)
    l_posl = get_posl(prel[1:i+1], inl[:i])
    r_posl = get_posl(prel[i+1:], inl[i+1:])
    return l_posl + r_posl + [root]
    
if __name__ == "__main__":
    s = []
    for _ in range(2*N):
        input_l = input().split()
        if input_l[0] == "Push":
            s.append(int(input_l[1]))
            prel.append(int(input_l[1]))
        else:
            inl.append(s.pop())
    
    posl = get_posl(prel, inl)
    
    print(' '.join(map(str, posl)))