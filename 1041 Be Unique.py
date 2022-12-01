l = list(map(int, input().split()[1:]))
count = [0 for _ in range(100001)]

for i in l:
    count[i] += 1
for i in l:
    if count[i] == 1:
        print(i)
        break
else:
    print("None")