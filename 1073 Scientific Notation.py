s = input()

e = int(s[s.index('E')+1:])    # 指数,存为整型
f = s[1:s.index('E')]          # 有效数字部分(不带符号),存为字符串 如"1.2"

if e < 0:
    c = "0." + '0'*(-e-1) + f.replace('.', '')   # 小数点左移,整数部分只可能为1位且不为0
else:
    fs = len(f[f.index('.')+1:])
    if fs > e:                                   # 小数点右移,但未超过有效数字部分,也就是说最后输出的字符串还包含小数点
        l = list(f.replace('.', ''))
        l.insert(-(fs-e), '.')
        c = ''.join(l)
    else:                                        # 小数点右移,超过有效数字部分,每超1位就加个0
        c = f.replace('.', '') + '0'*(e-fs)

if s[0] == '-':
    print('-' + c)
else:
    print(c)

