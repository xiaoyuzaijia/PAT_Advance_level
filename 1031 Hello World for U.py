s = list(input())

n1 = (len(s) + 2) // 3
n2 = (len(s) - 2 * n1) + 2

for _ in range(n1 - 1):
    print(s.pop(0) + ' '*(n2-2) + s.pop())
print(''.join(s))