N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if __name__ == "__main__":
    for i in range(1, N):
        if b == list(sorted(a[:i+1])) + a[i+1:]:
            print("Insertion Sort")
            next_l = list(sorted(a[:i+2])) + a[i+2:]
            print(' '.join(map(str, next_l)), end='')
            exit(0)
    
    i = 2
    while i <= N:
        current_l = []
        for j in range(0, N, i):
            current_l.extend(list(sorted(a[j:j+i])))
        if b == current_l:
            print("Merge Sort")
            break
        i *= 2
    
    i *= 2
    next_l = []
    for j in range(0, N, i):
        next_l.extend(list(sorted(a[j:j+i])))
    print(' '.join(map(str, next_l)), end='')