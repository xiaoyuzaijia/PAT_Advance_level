import math

N, A, B = input().split()
N = int(N)

def chop(a):
    if float(a) == 0.0:
        return "0." + '0'*N + "*10^0"
    
    if float(a) < 1:        # 小于1的数
        a_s = "0." + a.replace('.', '').strip('0')[:N]
        e = 0
        for i in a[a.find('.')+1:]:
            if i == '0':
                e -= 1
            else:
                break
        e_s = f"10^{e}"
    else:                   # 大于等于1的数
        a = a.lstrip('0')
        a_s = "0." + a.replace('.', '').strip('0')[:N]
        if a.find('.') != -1:
            e = a.find('.')
        else:
            e = len(a)
        e_s = f"10^{e}"
    
    if len(a_s) < N + 2:
        a_s += '0' * (N + 2 - len(a_s))
    
    
    
    return a_s + '*' + e_s

if __name__ == "__main__":
    A = chop(A)
    B = chop(B)
    
    if A == B:
        print("YES", A)
    else:
        print("NO", A, B)


'''
世上最坑测试点,代码也是纯纯屎山...
'''