N1, N2, tag, radix1 = input().split()
value = dict(zip("0123456789abcdefghijklmnopqrstuvwxyz", range(36)))

def trans(a, radix):  # 进制转换,转换成十进制(radix是基数, 基数是可能大于36的)
    d = 0
    
    for e, i in enumerate(reversed(a)):
        d += value[i] * (radix ** e)
    
    return d

def find(left, right):
    if left > right:
        return False
    else:
        mid = (left + right) // 2
        if trans(N2, mid) == N1_value:
            return mid
        elif trans(N2, mid) < N1_value:
            return find(mid+1, right)
        else:
            return find(left, mid-1)
        
        
if __name__ == "__main__":
    if tag == '2':
        N1, N2 = N2, N1
    
    N1_value = trans(N1, int(radix1))
    radix2_left = max(N2, key=lambda x: value[x])    # 二分下界
    radix2_left = value[radix2_left] + 1 if value[radix2_left] + 1 >= 2 else 2
    radix2_right = N1_value + 1 if N1_value + 1 >= 2 else 2     # 二分上界
    
    found = find(radix2_left, radix2_right)
    if found:
        print(found)
    else:
        print("Impossible")