N, K = map(int, input().split())
info = [[] for _ in range(2501)]

if __name__ == "__main__":
    for _ in range(N):
        input_l = input().split()
        id_ = input_l.pop(0)
        cos = list(map(int, input_l))
        for i in cos[1:]:
            info[i].append(id_)
    
    for i in range(1, K+1):
        if not info[i]:
            print(i, 0)
        else:
            print(i, len(info[i]))
            info[i].sort()
            print('\n'.join(info[i]))