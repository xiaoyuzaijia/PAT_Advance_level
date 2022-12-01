N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
Level_leaf = []

def bfs(s):
    q = [s]
    
    leaf = 0
    last = s
    while q:
        v = q.pop(0)
        if not G[v]:
            leaf += 1
        
        for w in G[v]:
            q.append(w)
            rear = w
        
        if last == v:
            Level_leaf.append(leaf)
            leaf = 0
            last = rear
    
    
if __name__ == "__main__":
    if M == 0:
        print(1)
        exit(0)
    
    for _ in range(M):
        input_l = list(map(int, input().split()))
        v = input_l[0]
        ws = input_l[2:]
        G[v].extend(ws)
    
    bfs(1)

    print(' '.join(list(map(str, Level_leaf))))