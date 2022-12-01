N, L = map(int, input().split())
G = [[] for _ in range(N)]


def BFS(s):
    visi = [False for _ in range(N)]
    visi[s] = True
    cnt = 0
    
    q = [s]
    level = 0
    l_last = s
    last = s
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visi[w]:
                visi[w] = True
                q.append(w)
                cnt += 1
                last = w
        
        if v == l_last:
            level += 1
            l_last = last
        
        if level == L:
            break
    
    return cnt

if __name__ == "__main__":
    for w in range(N):
        for v in list(map(int, input().split()[1:])):
            G[v-1].append(w)
    
    for v in list(map(int, input().split()[1:])):
        print(BFS(v-1))
        