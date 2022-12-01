a = input()
b = input()

l = []
j = 0
for i in range(len(a)):
    if j < len(b) and a[i] == b[j]:
        j += 1
    else:
        if a[i].upper() not in l:
            l.append(a[i].upper())
    
print(''.join(l))