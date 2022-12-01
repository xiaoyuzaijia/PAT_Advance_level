input_l = list(map(int, input().split()))       
N = input_l[0]
l = input_l[1:]


if __name__ == "__main__":
    swaps = 0
    
    for i in range(1, N):
        if l[i] != i:
            while l[0] != 0:
                t = l[0]
                l[0], l[t] = l[t], l[0]
                swaps += 1
            if l[i] != i:
                l[0], l[i] = l[i], l[0]
                swaps += 1
    
    
    print(swaps)


'''
输入样例展示有误,应为
10 3 5 7 2 6 4 9 0 8 1
而不是
10
3 5 7 2 6 4 9 0 8 1
不然python提交会非零返回
'''