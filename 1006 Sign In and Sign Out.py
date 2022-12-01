M = int(input())
Record_d = {}

if __name__ == "__main__":
    for _ in range(M):
        id_, sign_in, sign_out = input().split()
        sign_in = tuple(map(int, sign_in.split(':')))
        sign_out = tuple(map(int, sign_out.split(':')))
        Record_d[id_] = (sign_in, sign_out)
    
    earilest_id = min(Record_d.keys(), key=lambda x: Record_d[x][0])
    lastest_id = max(Record_d.keys(), key=lambda x: Record_d[x][1])
    print(earilest_id, lastest_id)