import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

def decimal_to_radix(n, radix):
    r = ''
    
    while n:
        r = str(n%radix) + r
        n //= radix
    
    return r

def check(n, radix):
    if not is_prime(n):
        return False
    r = decimal_to_radix(n, radix)
    r = r[::-1]
    r = int(r, radix)
    if is_prime(r):
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        input_l = list(map(int, input().split()))
        if input_l[0] < 0:
            break
        
        n, radix = input_l
        if check(n, radix):
            print("Yes")
        else:
            print("No")