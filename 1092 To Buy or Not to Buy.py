s = input()
n = input()

shop = {}
need = {}

for i in s:
    if i not in shop:
        shop[i] = 1
    else:
        shop[i] += 1
for i in n:
    if i not in need:
        need[i] = 1
    else:
        need[i] += 1

mis = 0
for i in need.keys():
    if i not in shop:
        mis += need[i]
    elif shop[i] < need[i]:
        mis += need[i] - shop[i]

if mis > 0:
    print("No", mis)
else:
    print("Yes", len(s)-len(n))

