MAX_DIST = 100000
Cmax, N, Sp, M = map(int, input().split())
G = [[] for _ in range(N+1)]
E = {}
Path = [0 for _ in range(N+1)]
Need = [0 for _ in range(N+1)]
Back = [0 for _ in range(N+1)]
BIKES = [0 for _ in range(N+1)]

def find_min(dist, collect):
    min_disst = MAX_DIST
    min_v = -1
    
    for v in range(N+1):
        if not collect[v] and dist[v] < min_disst:
            min_disst = dist[v]
            min_v = v
    
    return min_v

def Dijkstra(s):
    dist = [MAX_DIST for _ in range(N+1)]
    collect = [False for _ in range(N+1)]
    collect[s] = True
    for w in G[s]:
        dist[w] = E[(s,w)]
        Path[w] = s
        if BIKES[w] <= Cmax // 2:
            Need[w] = Cmax // 2 - BIKES[w]
        elif BIKES[w] > Cmax // 2:
            Back[w] = BIKES[w] - Cmax // 2
    
    while True:
        v = find_min(dist, collect)
        if v == -1:
            break
        
        collect[v] = True
        for w in G[v]:
            if not collect[w]:
                if dist[w] > dist[v] + E[(v,w)]:
                    dist[w] = dist[v] + E[(v,w)]
                    Path[w] = v
                    if BIKES[w] >= Cmax // 2:
                        Need[w] = Need[v]
                        Back[w] = Back[v] + (BIKES[w] - Cmax//2)
                    else:
                        if Back[v] >= Cmax // 2 - BIKES[w]:
                            Need[w] = Need[v]
                            Back[w] = Back[v] - (Cmax // 2 - BIKES[w])
                        else:
                            Need[w] = Need[v] + (Cmax // 2 - BIKES[w]) - Back[v]
                            Back[w] = 0
                elif dist[w] == dist[v] + E[(v,w)]:
                    if BIKES[w] >= Cmax // 2:
                        Need2 = Need[v]
                        Back2 = Back[v] + (BIKES[w] - Cmax//2)
                    else:
                        if Back[v] >= Cmax // 2 - BIKES[w]:
                            Need2 = Need[v]
                            Back2 = Back[v] - (Cmax // 2 - BIKES[w])
                        else:
                            Need2 = Need[v] + (Cmax // 2 - BIKES[w]) - Back[v]
                            Back2 = 0
                    if (Need[w], Back[w]) >= (Need2, Back2):
                        Need[w], Back[w] = Need2, Back2
                        Path[w] = v

if __name__ == "__main__":
    BIKES = [0] + list(map(int, input().split()))
    
    for _ in range(M):
        a, b, w = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        E[(a, b)] = w
        E[(b, a)] = w
    
    Dijkstra(0)
    
    shortest_path = [Sp]
    v = Sp
    while v:
        v = Path[v]
        shortest_path.append(v)
    shortest_path.reverse()
    
    print(Need[Sp], '->'.join(list(map(str, shortest_path))), Back[Sp])

'''
最后一个测试点超时
'''