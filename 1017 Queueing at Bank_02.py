N, K = map(int, input().split())
customers = []
ws_freetick = [8*3600 for _ in range(K)]

def ticks_from_zero(hms):
    return hms[0] * 3600 + hms[1] * 60 + hms[2]

if __name__ == "__main__":
    for _ in range(N):
        hms, p = input().split()
        arr_tick = ticks_from_zero(tuple(map(int, hms.split(':'))))
        if arr_tick <= 17 * 3600:
            p = int(p) * 60
            customers.append((arr_tick, p))
    
    customers.sort()
    
    served_customer_num = len(customers)
    total_wait_ticks = 0
    
    for customer in customers:
        ws_freetick.sort()
        if customer[0] < ws_freetick[0]:                #到达时没有空闲的窗口
            total_wait_ticks += ws_freetick[0] - customer[0]
            ws_freetick[0] += customer[1]                   #空闲时刻更新为之前的空闲时刻加这个人的处理时间
        else:                                           #到达时有空闲窗口
            ws_freetick[0] = customer[0] + customer[1]      #空闲时刻更新为这个人的到达时刻加这个人的处理时间
    
    print(f"{total_wait_ticks/60/served_customer_num:.1f}")


'''
思路
https://blog.csdn.net/liu1008611/article/details/82382175?ops_request_misc=&request_id=&biz_id=102&utm_term=1017%20python&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-82382175.142^v50^control_1,201^v3^control_1&spm=1018.2226.3001.4187
'''