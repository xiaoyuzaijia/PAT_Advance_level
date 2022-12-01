M, N, K = map(int, input().split())

def check(q):
    in_s = list(range(N, 0, -1))
    s = []
    
    while q:
        if s and s[-1] == q[-1]:
            s.pop()
            q.pop()
        elif in_s:
            s.append(in_s.pop())
            if len(s) > M:
                return False
        elif not in_s:
            return False
    return True

if __name__ == "__main__":
    for _ in range(K):
        q = list(map(int, input().split()))
        q.reverse()
        if check(q):
            print("YES")
        else:
            print("NO")