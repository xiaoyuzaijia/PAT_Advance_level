N, K, s = input().split()
N = int(N)
K = int(K)
G = {}
E = {}
H = {}

dist = {}
hs = {}  # 幸福值列表
path = {}
routes = {} #　最短路条数

def find_min(vis):
    min_d = 1e5
    min_v = -1
    
    for v in G.keys():
        if not vis[v] and min_d > dist[v]:
            min_d = dist[v]
            min_v = v
    
    return min_v

def dijkstra(s):
    vis = dict(zip(G.keys(), [False]*N))
    
    vis[s] = True
    dist[s] = 0
    for v in G[s]:
        dist[v] = E[(s,v)]
        hs[v].append(H[v])
        path[v] = s
    
    
    while True:
        v = find_min(vis)
        vis[v] = True
        if v == -1:
            break
        
        for w in G[v]:
            if not vis[w]:
                if dist[w] > dist[v] + E[(v,w)]:
                    routes[w] = routes[v]
                    dist[w] = dist[v] + E[(v,w)]
                    hs[w] = hs[v] + [H[w]]
                    path[w] = v
                elif dist[w] == dist[v] + E[(v,w)]:
                    routes[w] += routes[v]
                    if sum(hs[w]) < sum(hs[v]) + H[w]:
                        dist[w] = dist[v] + E[(v,w)]
                        hs[w] = hs[v] + [H[w]]
                        path[w] = v
                    elif sum(hs[w]) == sum(hs[v]) + H[w]:
                        if sum(hs[w])/len(hs[w]) < (sum(hs[v]) + H[w])/(len(hs[v])+1):
                            dist[w] = dist[v] + E[(v,w)]
                            hs[w] = hs[v] + [H[w]]
                            path[w] = v
    
    

if __name__ == "__main__":
    G[s] = []
    dist[s] = 0
    hs[s] = []
    path[s] = -1
    routes[s] = 1
    for _ in range(N-1):
        c, h = input().split()
        H[c] = int(h)
        
        G[c] = []
        dist[c] = 1e5
        hs[c] = []
        path[c] = -1
        routes[c] = 1
    
    for _ in range(K):
        v, w, e = input().split()
        G[v].append(w)
        G[w].append(v)
        E[(v, w)] = int(e)
        E[(w, v)] = int(e)
    
    dijkstra(s)
    
    print(routes["ROM"], dist["ROM"], sum(hs["ROM"]), sum(hs["ROM"])//len(hs["ROM"]))
    v = "ROM"
    path_l = []
    while v != -1:
        path_l.append(v)
        v = path[v]
    print("->".join(reversed(path_l)))