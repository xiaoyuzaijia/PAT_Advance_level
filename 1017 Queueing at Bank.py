N, K = map(int, input().split())
customers = []    #所有人
out_line = []     #进入银行的人
ws = [None for _ in range(K)]

def ticks_from_zero(hms):
    return hms[0] * 3600 + hms[1] * 60 + hms[2]

if __name__ == "__main__":
    for _ in range(N):
        hms, p = input().split()
        arr_tick = ticks_from_zero(tuple(map(int, hms.split(':'))))
        p = int(p) * 60
        customers.append([arr_tick, p])
    
    customers.sort(reverse=True)
    
    total_wait_ticks = 0
    served_customer_num = 0
    
    while customers[-1][0] < 28800:   #8 * 3600    #8:00前进入银行
        out_line.append(customers.pop())
    
    tick = 28800
    while tick <= 61200:     #17 * 3600
        if customers and customers[-1][0] == tick:  #进入银行
            out_line.append(customers.pop())
        
        for i in range(K):              #到窗口
            if ws[i] is None and out_line:
                ws[i] = out_line.pop(0)
                served_customer_num += 1
                total_wait_ticks += tick - ws[i][0]
        
        for i in range(K):              #窗口办理
            if ws[i] is not None:
                ws[i][1] -= 1
                if ws[i][1] == 0:
                    ws[i] = None
        
        tick += 1
    
    while out_line:       #17:00之后不能再进人了,但已经在银行等待的人还要给他服务完
        for i in range(K):
            if ws[i] is None and out_line:
                ws[i] = out_line.pop(0)
                served_customer_num += 1
                total_wait_ticks += tick - ws[i][0]
        
        for i in range(K):
            if ws[i] is not None:
                ws[i][1] -= 1
                if ws[i][1] == 0:
                    ws[i] = None
        
        tick += 1
    
    print(f"{total_wait_ticks/60/served_customer_num:.1f}")

'''
5 运行超时 0 -- 4696 KB
'''