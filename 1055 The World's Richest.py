N, K = map(int, input().split())
info = []

def query(m, amin, amax):
    l = list(filter(lambda x: amin<=x[1]<=amax, info))

    if not l:
        print("None")
        return
    
    if m > len(l):
        m = len(l)
    for i in range(m):
        print(l[i][0], l[i][1], l[i][2])

if __name__ == "__main__":
    for _ in range(N):
        name, age, w = input().split()
        info.append((name, int(age), int(w)))
    
    info.sort(key=lambda x: (-x[2], x[1], x[0]))

    for i in range(1, K+1):
        print(f"Case #{i}:")
        query(*map(int, input().split()))


'''
两个测试点超时...
'''