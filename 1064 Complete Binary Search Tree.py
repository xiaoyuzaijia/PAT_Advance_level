N = int(input())
t = [-1 for _ in range(N+1)]

def inorder_t(i):
    if i <= N:
        inorder_t(i*2)
        t[i] = inl.pop()
        inorder_t(i*2+1)

if __name__ == "__main__":
    inl = list(map(int, input().split()))
    inl.sort(reverse=True)
    
    inorder_t(1)
    
    print(' '.join(map(str, t[1:])))