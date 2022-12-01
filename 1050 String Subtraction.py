s1 = input()
s2 = input()    # 字符串的in操作比列表的快

s1 = filter(lambda x: x not in s2, s1)

print(''.join(s1))