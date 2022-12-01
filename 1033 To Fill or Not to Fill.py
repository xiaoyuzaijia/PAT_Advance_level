MAX_NUM = 100000
Cmax, D, Davg, N = map(int, input().split())
Price = []
Dist = []


if __name__ == "__main__":
    info = []
    for _ in range(N):
        p, d = input().split()
        info.append((float(p), int(d)))
    info.sort(key=lambda x: x[1])
    
    Price = [i[0] for i in info]
    Dist = [i[1] for i in info] + [D]
    
    cp = [0 for i in range(N+1)]
    if Dist[0] == 0:
        cp[0] = 0
    else:
        print("The maximum travel distance = 0")
        exit(0)
    
    for i in range(1, N+1):
        min_p = MAX_NUM
        
        for j in range(0, i):
            if Dist[i] - Dist[j] <= Cmax * Davg:
                if min_p > cp[j] + ((Dist[i] - Dist[j]) / Davg) * Price[j]:
                    min_p = cp[j] + ((Dist[i] - Dist[j]) / Davg) * Price[j]
        
        if min_p == MAX_NUM:
            print(f"The maximum travel distance = {Dist[i-1]+Cmax * Davg:.2f}")
            exit(0)
        else:
            cp[i] = min_p
    
    print(f"{cp[-1]:.2f}")
    print(cp)


'''
想法错了....
'''