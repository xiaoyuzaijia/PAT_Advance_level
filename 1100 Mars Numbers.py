N = int(input())
a1 = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
a2 = ["tret", "tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]


def deci_to_base(n):
    s = ""
    if n%13 == 0:
        return a2[n//13]
    s = a1[n%13] + s
    if n//13 > 0:
        s = a2[n//13] + ' ' + s
    return s

def base_to_deci(sl):
    n = 0
    for i in sl:
        if i in a1:
            n += a1.index(i)
        else:
            n += a2.index(i)*13
    return n

if __name__ == "__main__":
    for _ in range(N):
        n = input()
        if n.isdigit():
            print(deci_to_base(int(n)))
        else:
            print(base_to_deci(n.split()))