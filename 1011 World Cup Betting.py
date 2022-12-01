g1 = map(float, input().split())
g2 = map(float, input().split())
g3 = map(float, input().split())
wtl = ['W', 'T', 'L']
gres_l=[]
odd_l = []

if __name__ == "__main__":
    for g in (g1, g2 ,g3):
        max_odd = 0
        for i, odd in enumerate(g):
            if odd > max_odd:
                gres = wtl[i]
                max_odd = odd
        odd_l.append(max_odd)
        gres_l.append(gres)
        
    profit = 1.0
    for odd in odd_l:
        profit *= odd
    profit = (profit * 0.65 - 1) * 2

    print(' '.join(gres_l), end='')
    print(f" {profit:.2f}")