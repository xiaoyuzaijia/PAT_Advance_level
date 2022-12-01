N, M = map(int, input().split())
G = [[] for _ in range(N)]
max_n = 0
max_l = 1

def BFS(s):
    global max_n, max_l
    
    vis = [False for _ in range(N)]
    vis[s] = True
    q = [s]
    level = 1
    last = s
    l_last = s
    l_n = 0
    
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not vis[w]:
                vis[w] = True
                q.append(w)
                l_n += 1
                last = w
        
        if v == l_last:
            l_last = last
            level += 1
            if max_n < l_n:
                max_n = l_n
                max_l = level
            l_n = 0

if __name__ == "__main__":
    if N == 1:
        print(1, 1)
        exit(0)
    
    for _ in range(M):
        input_l = list(map(int, input().split()))
        v = input_l[0] - 1
        k = input_l[1]
        G[v] = [i-1 for i in input_l[2:]]
    
    BFS(0)
    
    print(max_n, max_l)