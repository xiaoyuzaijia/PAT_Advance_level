def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def out(a, b):
    sign = 0
    if a < 0:
        sign = 1
        a = -a
    
    mc = gcd(a, b)
    a //= mc
    b //= mc
    
    if sign == 1:
        print("(-", end='')
    if a == 0:
        print(0, end='')
    elif a >= b:
        print(a//b, end='')
        if a%b != 0:
            print(f" {a%b}/{b}", end='')
    else:
        print(f"{a%b}/{b}", end='')
    if sign == 1:
        print(')', end='')
    
    

    
def add(a1, a2, b1, b2):
    c1 = a1*b2 + a2*b1
    c2 = a2*b2
    
    return (c1, c2)


def mul(a1, a2, b1, b2):
    c1 = a1*b1
    c2 = a2*b2
    
    return (c1, c2)


if __name__ == "__main__":
    input_l = input().split()
    a1, a2 = map(int, input_l[0].split('/'))
    b1, b2 = map(int, input_l[1].split('/'))
    
    out(a1, a2)
    print(" + ", end='')
    out(b1, b2)
    print(" = ", end='')
    out(*add(a1, a2, b1, b2))
    print()
    
    out(a1, a2)
    print(" - ", end='')
    out(b1, b2)
    print(" = ", end='')
    out(*add(a1, a2, -b1, b2))
    print()
    
    out(a1, a2)
    print(" * ", end='')
    out(b1, b2)
    print(" = ", end='')
    out(*mul(a1, a2, b1, b2))
    print()
    
    out(a1, a2)
    print(" / ", end='')
    out(b1, b2)
    print(" = ", end='')
    if b1 == 0:
        print("Inf", end='')
    elif b1 > 0:
        out(*mul(a1, a2, b2, b1))
    else:
        out(*mul(a1, a2, -b2, -b1))
    print()
