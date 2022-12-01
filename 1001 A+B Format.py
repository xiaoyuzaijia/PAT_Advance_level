a, b = map(int, input().split())

c = a + b
if c >= 0:
    c = list(str(c))
    for i in range(len(c)-3, 0, -3):
        c.insert(i, ',')
    print(''.join(c))
else:
    c = -c
    c = list(str(c))
    for i in range(len(c)-3, 0, -3):
        c.insert(i, ',')
    print('-'+''.join(c))