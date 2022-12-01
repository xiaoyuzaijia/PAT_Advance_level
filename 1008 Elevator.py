input_l = list(map(int, input().split()))
N = input_l[0]
request_l = input_l[1:]

if __name__ == "__main__":
    current = 0
    total_time = 0
    for i in request_l:
        if i > current:
            total_time += 6 * (i - current)
        else:
            total_time += 4 * (current - i)
        current = i
        total_time += 5
    
    print(total_time)