Nodes = [[None, -1, 0] for _ in range(100000)]   # [key, next, flag]
S1, S2, N = map(int, input().split())

if __name__ == "__main__":
    for _ in range(N):
        add, key, next = input().split()
        Nodes[int(add)][0:2] = key, int(next)
        
    node = S1
    while node != -1:
        Nodes[node][2] = 1
        node = Nodes[node][1]
    
    node = S2
    while node != -1:
        if Nodes[node][2] == 1:
            print(f"{node:>05d}")
            exit(0)
        node = Nodes[node][1]
    
    print(-1)


'''
5 运行超时 0 -- 19188 KB
'''