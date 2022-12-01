N = int(input())
info = []

for _ in range(N):
    n, p = input().split()
    mp = p.replace('1', '@').replace('0', '%').replace('l', 'L').replace('O', 'o')
    if mp != p:
        info.append((n, mp))


if not len(info) :
    if N == 1:
        print("There is 1 account and no account is modified")
    else:
        print(f"There are {N} accounts and no account is modified")
else:
    print(len(info))
    for n, mp in info:
        print(n, mp)
