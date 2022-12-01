N = input()


count = 0
a = 1
for i in range(len(N)-1, -1, -1):
    l = int(N[:i]) if N[:i] else 0
    n = int(N[i])
    r = int(N[i+1:]) if N[i+1:] else 0
    if n == 0:
        count += l * a
    elif n == 1:
        count += l * a + r + 1
    else:
        count += (l + 1) * a
    a *= 10

print(count)


'''
https://blog.csdn.net/liuchuo/article/details/52264944
'''