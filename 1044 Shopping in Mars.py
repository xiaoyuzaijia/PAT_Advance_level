N, M = map(int, input().split())
cl = [0] + list(map(int, input().split()))
s = [0]
for i in cl[1:]:
    s.append(s[-1] + i)

def two_find(l, r):
    i = l
    while l < r:
        mid = (l + r) // 2
        if s[mid] - s[i-1] == M:
            return mid
        elif s[mid] - s[i-1] > M:
            r = mid
        else:
            l = mid + 1
    return r

if __name__ == "__main__":
    min_cha = 100000
    ij_l = []
    for i in range(1, N+1):
        j = two_find(i, N)
        if s[j] - s[i-1] >= M:
            if min_cha > s[j] - s[i-1] - M:
                min_cha = s[j] - s[i-1] - M
                ij_l.clear()
            if min_cha == s[j] - s[i-1] - M:
                ij_l.append((i, j))
    
    for i in range(len(ij_l)):
        if i == len(ij_l)-1:
            print(f"{ij_l[i][0]}-{ij_l[i][1]}", end='')
        else:
            print(f"{ij_l[i][0]}-{ij_l[i][1]}")


'''
三个测试点超时...
''' 