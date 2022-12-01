import math
n = int(input())
f = {}

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1 , 2):
            if n % i == 0:
                return False
        return True

if __name__ == "__main__":
    m = n
    while m != 1:
        for i in range(2, m+1):
            if is_prime(i) and m % i == 0:
                if i not in f:
                    f[i] =0
                f[i] += 1
                m //= i
                break
    
    ans = []
    for i in sorted(f.keys()):
        if f[i] == 1:
            ans.append(str(i))
        else:
            ans.append(str(i) + '^' + str(f[i]))
    
    if n == 1:
        ans = ['1']
    print(f"{n}=" + '*'.join(ans))