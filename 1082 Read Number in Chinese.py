n = list(input())
pn = "ling yi er san si wu liu qi ba jiu".split()


def read4(n):
    read = []
    d = ["Qian", "Bai", "Shi"]
    
    flag = 0
    if len(n) < 4:
        n = ['0'] * (4-len(n)) + n
        flag = 1
    
    for i in range(3):
        if all([x == '0' for x in n[i:]]):
            if flag == 1:
                read.pop(0)
            return read
        elif n[i] == '0':
            if not read or read[-1] != "ling":
                read.append("ling")
        else:
            read.append(pn[int(n[i])])
            read.append(d[i])
    if n[3] != '0':
        read.append(pn[int(n[3])])
    
    if flag == 1:
        read.pop(0)
    
    return read

if __name__ == "__main__":
    if n[0] == '-':
        print("Fu ", end='')
        n.pop(0)
    
    if n == ['0']:
        print("ling")
        exit(0)
    
    pd = ["Yi", "Wan"]
    read = []
    
    for i in range(len(n)//4+1):
        l = len(n)-i*4-4
        r = len(n)-i*4
        if l < 0:
            l = 0
        if n[l:r]:
            if i == 0:
                read = read4(n[l:r]) + read
            elif i == 1:
                read = read4(n[l:r]) + ["Wan"] + read
            else:
                read = read4(n[l:r]) + ["Yi"] + read
    
    print(' '.join(read))
    
    

'''
这种题目写出来就是纯纯屎山...
'''