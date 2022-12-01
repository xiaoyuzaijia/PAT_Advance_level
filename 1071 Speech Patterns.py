t = input().lower() # 大写字母换成小写
alp = "0123456789abcdefghijklmnopqrstuvwxyz"
t = ''.join(map(lambda x: ' ' if x not in alp else x, t))  # 将所有不在alp字符表里字符的都换成空格
d = {}

if __name__ == "__main__":
    l = t.split()
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    m_c = max(d.keys(), key=lambda x: (d[x], x[::-1]))
    print(m_c, d[m_c])