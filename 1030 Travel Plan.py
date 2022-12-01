MAX_NUM = 100000
N, M, S, D = map(int, input().split())
G = [[] for _ in range(N)]
E = {}
C = {}
Path = [0 for _ in range(N)]
Dist = [MAX_NUM for _ in range(N)]
Cost = [MAX_NUM for _ in range(N)]

def find_min(collect):
    min_dist = MAX_NUM
    mini_v = -1
    
    for v in range(N):
        if not collect[v]:
            if min_dist > Dist[v]:
                min_dist = Dist[v]
                mini_v = v
    
    return mini_v

def Dijkstra(s):
    collect = [False for _ in range(N)]
    collect[s] = True
    
    for w in G[s]:
        Path[w] = s
        Dist[w] = E[(s,w)]
        Cost[w] = C[(s,w)]
    
    while True:
        v = find_min(collect)
        if v == -1:
            break
        collect[v] = True
        
        for w in G[v]:
            if not collect[w]:
                if Dist[w] > Dist[v] + E[(v,w)]:
                    Dist[w] = Dist[v] + E[(v,w)]
                    Cost[w] = Cost[v] + C[(v,w)]
                    Path[w] = v
                elif Dist[w] == Dist[v] + E[(v,w)]:
                    if Cost[w] > Cost[v] + C[(v,w)]:
                        Cost[w] = Cost[v] + C[(v,w)]
                        Path[w] = v


if __name__ == "__main__":
    for _ in range(M):
        a, b, d, c = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        E[(a,b)] = d
        E[(b,a)] = d
        C[(a,b)] = c
        C[(b,a)] = c
    
    Dijkstra(S)
    
    shortest_path_l = [D]
    v = D
    while v != S:
        v = Path[v]
        shortest_path_l.append(v)
    shortest_path_l.reverse()
    
    print(' '.join(list(map(str, shortest_path_l))), Dist[D], Cost[D])