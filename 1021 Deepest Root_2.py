N = int(input())
G = [[] for _ in range(N)]
visited = [False for _ in range(N)]
Height = {}

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
        Height[v] = deep

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

    visited = [False for _ in range(N)]
    DFS_deep(0, 1)                           # 从0节点开始找到离他最远的所有节点（可能不止一个，记为集合A）
    max_height = max(Height.values())
    a = list(filter(lambda x: Height[x] == max_height, Height.keys()))

    visited = [False for _ in range(N)]
    Height = {}
    DFS_deep(a[0], 1)                        # 从集合A选一个节点到离他最远的所有节点（可能不止一个，记为集合B）
    max_height = max(Height.values())
    b = list(filter(lambda x: Height[x] == max_height, Height.keys()))

    a = set(a)
    b = set(b)
    deepest_roots = list(a | b)              # 取集合A和集合B并集
    deepest_roots.sort()

    for v in deepest_roots:
        print(v+1)


'''
思路
https://blog.csdn.net/wwang_dev/article/details/106125559?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166445438816782414946294%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall%255Fv2.%2522%257D&request_id=166445438816782414946294&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all_v2~first_rank_ecpm_v1~rank_v31_ecpm-11-106125559-null-null.142^v51^control_1,201^v3^control_1&utm_term=1021%20Deepest%20Root&spm=1018.2226.3001.4187
'''
