Nc = int(input())
c = list(map(int, input().split()))
Np = int(input())
p = list(map(int, input().split()))

c.sort()
p.sort()
m = 0
while (c and p) and (c[-1] > 0 and p[-1]) > 0:
    m += c.pop() * p.pop()
c.reverse()       # reverse一下方便pop(),节省时间.不然pop(0)可能会超时
p.reverse()
while (c and p) and (c[-1] < 0 and p[-1]) < 0:
    m += c.pop() * p.pop()

print(m, end='')