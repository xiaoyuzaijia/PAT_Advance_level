M, N = map(int, input().split())
d = {}

for _ in range(N):
    for i in map(int, input().split()):
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

c = max(d, key=lambda x:d[x])
print(c)