N, M, K, Q = map(int, input().split())

def is_full_in_line(in_line):
    return len(list(filter(lambda x: len(x)>=M, in_line))) >= N

def get_hm(tick):
    return (8+tick//60, tick%60)

if __name__ == "__main__":
    process_time = list(map(int, input().split()))
    in_line = [[]for _ in range(N)]     # 黄线内的队伍,N个队列
    out_line = [i for i in range(K)]    # 黄线外的队伍,按客户编号
    finish_time = {}
    
    tick = 1
    while tick < 540:
        while out_line and (not is_full_in_line(in_line)):
            min_line = min(in_line, key=lambda x: len(x))
            min_line.append(out_line.pop(0))
        
        for line in in_line:
            if line:
                process_time[line[0]] -= 1
                if process_time[line[0]] == 0:
                    finish_time[line.pop(0)] = tick
        
        tick += 1
    
    for line in in_line:   # 服务到一半的,服务完才能下班
        if line:
            finish_time[line[0]] = tick + process_time[line[0]] - 1
    
    for i in map(lambda x: int(x)-1, input().split()):
        if i in finish_time:
            h, m = get_hm(finish_time[i])
            print(f"{h:02}:{m:02}")
        else:
            print("Sorry")