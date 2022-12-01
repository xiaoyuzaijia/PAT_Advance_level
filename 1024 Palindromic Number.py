N, K = map(int, input().split())

if __name__ == "__main__":
    i = 0
    while i < K and str(N) != str(N)[::-1]:
        N += int(str(N)[::-1])
        i += 1
    
    print(N)
    print(i)