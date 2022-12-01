D = [0] + list(map(int, input().split()[1:]))
M = int(input())
cl = sum(D)
s = [0, 0]
for i in D[1:-1]:
    s.append(s[-1] + i)

if __name__ == "__main__":
    for _ in range(M):
        i, j = map(int, input().split())
        if i > j:
            i, j = j, i
        
        if s[j] - s[i] < cl / 2:
            print(s[j] - s[i])
        else:
            print(cl - (s[j]-s[i]))