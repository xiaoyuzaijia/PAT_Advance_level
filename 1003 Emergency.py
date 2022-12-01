MAXDIST = 100000
N, M, S, D = map(int, input().split())
G = [[] for _ in range(N)]
Weight = {}
Hands = []


def find_min(visited, dist):
    mindist = MAXDIST
    minv = -1
    for v in range(N):
        if not visited[v] and dist[v] < mindist:
            minv = v
            mindist = dist[v]
    
    return minv

def dijkstra(s):
    visited = [False for _ in range(N)]
    dist = [MAXDIST for _ in range(N)]
    min_path_n = [0 for _ in range(N)]
    hands = Hands.copy()
    
    visited[s] = True
    min_path_n[s] = 1
    for v in G[s]:
        dist[v] = Weight[(s, v)]
        min_path_n[v] = 1
        hands[v] = hands[s] + Hands[v]
    
    
    while True:
        v = find_min(visited, dist)
        if v == -1:
            break
        visited[v] = True
        
        for w in G[v]:
            if not visited[w]:
                if dist[w] > dist[v] + Weight[(v,w)]:
                    dist[w] = dist[v] + Weight[(v,w)]
                    min_path_n[w] = min_path_n[v]
                    hands[w] = hands[v] + Hands[w]
                elif dist[w] == dist[v] + Weight[(v,w)]:
                    min_path_n[w] += min_path_n[v]        
                    if hands[w] < hands[v] + Hands[w]:    # 要判断hands更大才能加
                        hands[w] = hands[v] + Hands[w] 
    
    return min_path_n[D], hands[D]
    
if __name__ == "__main__":
    Hands = list(map(int, input().split()))
    for _ in range(M):
        a, b, weight = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        Weight[(a,b)] = Weight[(b,a)] = weight
    
    min_path_n, hands = dijkstra(S)
    print(min_path_n, hands)