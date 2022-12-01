N, C = map(int, input().split())
info = []

if __name__ == "__main__":
    for _ in range(N):
        id_, name, sc = input().split()
        info.append((int(id_), name, int(sc)))
    
    if C == 1:
        info.sort()
    elif C == 2:
        info.sort(key=lambda x: (x[1], x[0]))
    elif C == 3:
        info.sort(key=lambda x: (x[2], x[0]))
    
    for id_, name, sc in info:
        print(f"{id_:>06d} {name} {sc}")