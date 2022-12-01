toll = list(map(lambda x: float(x)/100, input().split()))
call = {}
month = 0

def fee_from_zero(t):  #从00:00:00开始的费用
    return t[0] * sum(toll) * 60 + sum(toll[:t[1]]) * 60 + toll[t[1]] * t[2]

def minutes_from_zero(t):  #从00:00:00开始的分钟数
    return t[0] * 24 * 60 + t[1] * 60 + t[2]

def fee(begin, end):
    return fee_from_zero(end) - fee_from_zero(begin)

def minutes(begin, end):
    return minutes_from_zero(end) - minutes_from_zero(begin)

if __name__ == "__main__":
    N = int(input())
    record_l = []
    for _ in range(N):
        id_, time, op = input().split()
        time = tuple(map(int, time.split(':')))
        if month == 0:            #记录月份,只要记录一次就行
            month = time[0]
        record_l.append((id_, time[1:], op))
    record_l.sort(key=lambda x: x[1])
    for id_, time, op in record_l:
        if op == "on-line":
            if id_ in call and len(call[id_][-1]) == 2:
                call[id_].append([time])
            elif id_ in call and len(call[id_][-1]) == 1:
                call[id_][-1][0] = time  # 如果上条记录是上线的，下条记录如果是上线则替换上条记录的上线时间 (这简直不合理)
            elif id_ not in call:
                call[id_] = [[time]]
        else:
            if id_ in call and len(call[id_][-1]) == 1:
                if call[id_][-1][0] != time: 
                    call[id_][-1].append(time)
                else:
                    call[id_].pop()       # 上线与下线时间一样,去掉这个记录
                    if not call[id_]:     # 如果去掉后,记录列表为空,则删掉这个id_ (不写这个的话29行会越界访问)
                        call.pop(id_)
    
    for id_ in sorted(call.keys()):
        if len(call[id_][-1]) == 1:  # 最后一次没有下线,去掉
            call[id_].pop()
        if not call[id_]:         # 没有记录,总费用为0,不输出
            continue
        
        print(f"{id_} {month:02}")
        total_fee = 0
        for begin, end in call[id_]:
            current_fee = fee(begin, end)
            total_fee += current_fee
            print(f"{begin[0]:02}:{begin[1]:02}:{begin[2]:02} {end[0]:02}:{end[1]:02}:{end[2]:02} {minutes(begin,end)} ${current_fee:.2f}")
        print(f"Total amount: ${total_fee:.2f}")


'''
这题太坑了,代码写得也跟屎山一样.不能直视
'''