N, K = map(int, input().split())
info = {}
query = []

for _ in range(K):
    c, n = map(int, input().split())
    if n == 0:
        continue
    for name in input().split():
        if name not in info:
            info[name] = []
        info[name].append(c)

query = input().split()

for name in query:
    if name not in info:
        print(name, 0)
    else:
        info[name].sort()
        print(name, len(info[name]), ' '.join(map(str, info[name])))