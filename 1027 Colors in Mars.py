R, G, B = map(int, input().split())
Digits = "0123456789ABC"

def trans_decimal_to_radix13(n:int):
    radix13_s = ''
    
    while n:
        radix13_s = Digits[n % 13] + radix13_s
        n //= 13
    
    return radix13_s

if __name__ == "__main__":
    r = trans_decimal_to_radix13(R)
    g = trans_decimal_to_radix13(G)
    b = trans_decimal_to_radix13(B)
    print(f"#{r:>02}{g:>02}{b:>02}")       # 字符串也可以格式化输出,>表示向右靠,不写可能会报错