def add(p1, p2):
    p = []
    
    while p1 and p2:
        if p1[0][0] == p2[0][0]:
            e = p1[0][0]
            c = p1.pop(0)[1] + p2.pop(0)[1]
            if c != 0:
                p.append((e, c))
        elif p1[0][0] > p2[0][0]:
            p.append(p1.pop(0))
        else:
            p.append(p2.pop(0))
    if p1:
        p.extend(p1)
    if p2:
        p.extend(p2)
    
    return p

def mul(p1, p2):
    p = []
    
    for e1, c1 in p1:
        for e2, c2 in p2:
            e = e1 + e2
            c = c1 * c2
            p = add(p, [(e,c)])
    
    return p


if __name__ == "__main__":
    input_l = input().split()
    P1 = []
    K1 = int(input_l[0])
    for i in range(1, 2*K1, 2):
        P1.append((int(input_l[i]), float(input_l[i+1])))
    input_l = input().split()
    P2 = []
    K2 = int(input_l[0])
    for i in range(1, 2*K2, 2):
        P2.append((int(input_l[i]), float(input_l[i+1])))
    
    p = mul(P1, P2)
    print(len(p), end='')
    for e, c in p:
        print(f" {e} {c:.1f}", end='')
    print()