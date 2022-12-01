A = []
B = []

def get_poly(p):
    input_l = input().split()
    k = int(input_l[0])
    for i in range(1, k+1):
        p.append((int(input_l[2*i-1]), float(input_l[2*i])))
    p.reverse()

def add(a, b):
    p = []
    while a and b:
        if a[-1][0] == b[-1][0]:
            e = a[-1][0]
            c = a.pop()[1] + b.pop()[1]
            if c != 0:
                p.append((e, c))
        elif a[-1][0] > b[-1][0]:
            p.append(a.pop())
        else:
            p.append(b.pop())
    if a:
        a.reverse()
        p.extend(a)
    if b:
        b.reverse()
        p.extend(b)
    return p

if __name__ == "__main__":
    get_poly(A)
    get_poly(B)
    P = add(A, B)
    print(len(P), end='')
    for e, c in P:
        print(f" {e} {c:.1f}", end='')
    print()