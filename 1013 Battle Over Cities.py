import copy
import heapq

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]

def BFS(s, visited, G):
    visited[s] = True
    q = []
    heapq.heappush(q, s)
    
    while q:
        v = heapq.heappop(q)
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                heapq.heappush(q, w)

def count_components(G, v):
    components = 0
    visited = [False for _ in range(N)]
    visited[v] = True
    
    for v in range(N):
        if not visited[v]:
            BFS(v, visited, G)
            components += 1
    
    return components


if __name__ == "__main__":
    for _ in range(M):
        v, w = map(int, input().split())
        G[v-1].append(w-1)
        G[w-1].append(v-1)
    
    for v in map(lambda x: int(x)-1, input().split()):
        G2 = copy.deepcopy(G)
        components = count_components(G2, v)
        print(components - 1)

'''
4 运行超时 0 -- 12080 KB
'''