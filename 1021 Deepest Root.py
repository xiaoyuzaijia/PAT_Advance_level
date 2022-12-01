N = int(input())
G = [[] for _ in range(N)]
visited = [False for _ in range(N)]
DEEP = [1 for _ in range(N)]

def DFS(v):
    if not visited[v]:
        visited[v] = True
        for w in G[v]:
            if not visited[w]:
                DFS(w)

def DFS_deep(v, deep):
    if not visited[v]:
        visited[v] = True
        for w in G[v]:
            if not visited[w]:
                DFS_deep(w, deep+1)      # 每递归一次深度加一
        DEEP[v] = max(DEEP[v], deep)     # 更新深度

if __name__ == "__main__":
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    
    components = 0                       # 计算连通集数量
    for v in range(N):
        if not visited[v]:
            DFS(v)
            components += 1
    if components > 1:
        print(f"Error: {components} components")
        exit(0)

    for v in range(N):                   # 对每个节点都作为起点DFS一次
        visited = [False for _ in range(N)]
        DFS_deep(v, 1)
    
    max_deep = max(DEEP)
    for v in range(N):
        if DEEP[v] == max_deep:
            print(v+1)

'''
3 运行超时 0 -- 4704 KB
'''
