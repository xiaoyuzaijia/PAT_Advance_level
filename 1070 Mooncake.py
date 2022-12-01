N, D = map(float, input().split())
inven = list(map(float, input().split()))
price = list(map(float, input().split()))
info = list(zip(inven, price))
info.sort(key=lambda x: x[1]/x[0], reverse=True)

if __name__ == "__main__":
    profit = 0
    for m, p in info:
        if m < D:
            profit += p
            D -= m
        else:
            profit += p * (D / m)
            break
    
    print(f"{profit:.2f}")