N, B = map(int, input().split())

def trans_to_baseB(n, b):
    l_base_b = []   #列表里的每个元素代表一位数
    
    while n:
        l_base_b.append(str(n % b))
        n //= b
    
    return l_base_b

if __name__ == "__main__":
    l = trans_to_baseB(N, B)
    if l == list(reversed(l)):
        print("Yes")
    else:
        print("No")
    print(' '.join(list(reversed(l))))