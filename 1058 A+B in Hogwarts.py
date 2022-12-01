a, b = input().split()
a = list(map(int, a.split('.')))
b = list(map(int, b.split('.')))

c = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
c[1] += c[2] // 29
c[2] = c[2] % 29
c[0] += c[1] // 17
c[1] = c[1] % 17

print('.'.join(map(str, c)))