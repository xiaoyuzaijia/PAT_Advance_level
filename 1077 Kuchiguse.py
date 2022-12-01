N = int(input())
l = []

for _ in range(N):
    l.append(input())

cnt = 0
for i in range(-1 , -len(l[0])-1, -1):
    s = l[0][i]
    if all([x[i]==s for x in l]):
        cnt += 1
    else:
        break

if cnt == 0:
    print("nai")
else:
    print(l[0][-cnt:])