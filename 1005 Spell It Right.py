s = sum(map(int, list(input())))
s = list(str(s))
d = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
s = map(lambda x: d[int(x)], s)
print(' '.join(s))