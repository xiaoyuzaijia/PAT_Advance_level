T = int(input())

for i in range(1, T+1):
    a, b, c = map(int, input().split())
    if i == T:
        if a + b > c:
            print(f"Case #{i}: true", end='')
        else:
            print(f"Case #{i}: false", end='')
    else:
        if a + b > c:
            print(f"Case #{i}: true")
        else:
            print(f"Case #{i}: false")