N = int(input())

if __name__ == "__main__":
    out_info = []               # 每个元素是(分数, id, 地区编号, 地区排名)
    
    for location_number in range(1, N+1):      # 地区编号,对每个地区处理
        k = int(input())
        
        local_info = []          # 每个元素是(分数, id)
        for _ in range(k):
            id_, sc = map(int, input().split())
            local_info.append((sc, id_))
        local_info.sort(key=lambda x: (-x[0], x[1]))
        
        current_rank = 0
        same_rank = 1
        last_sc = -1
        for sc, id_ in local_info:
            if last_sc != sc:
                current_rank += same_rank
                same_rank = 1
            else:
                same_rank += 1
            out_info.append((sc, id_, location_number, current_rank))
            last_sc = sc
    
    out_info.sort(key=lambda x: (-x[0], x[1]))
    print(len(out_info))
    
    current_rank = 0
    same_rank = 1
    last_sc = -1
    for sc, id_, location_number, local_rank in out_info:
        if last_sc != sc:
            current_rank += same_rank
            same_rank = 1
        else:
            same_rank += 1
        print(f"{id_:013d}", current_rank, location_number, local_rank)   # id是13位数字,前面补0,避免了当id是 000000000003 输入时,输出id的错误产生(测试点3)
        last_sc = sc