s1 = list(map(int, input().split()[1:]))
s2 = list(map(int, input().split()[1:]))

s = s1 + s2
s.sort()
print(s[(len(s)-1) // 2])