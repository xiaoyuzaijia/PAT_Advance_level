K = int(input())
shuff = list(map(int, input().split()))
deck = ['S'+str(i) for i in range(1,14)] + ['H'+str(i) for i in range(1,14)] + ['C'+str(i) for i in range(1,14)] + ['D'+str(i) for i in range(1,14)] + ["J1", "J2"]

def shuffl(deck, shuff):
    l = list(zip(shuff, deck))
    l.sort()
    
    return list(zip(*l))[1]

if __name__ == "__main__":
    for _ in range(K):
        deck = shuffl(deck, shuff)
    
    print(' '.join(deck))