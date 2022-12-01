N, M = map(int, input().split())
id_info = {}
id_ranks = {}

if __name__ == "__main__":
    for _ in range(N):
        id_, c, m, e = map(int, input().split())
        a = (c + m + e) / 3
        id_info[id_] = (a, c, m, e)
    for id_ in id_info.keys():
        id_ranks[id_] = [None, None, None, None]
    
    a_rank = sorted(id_info.keys(), key=lambda x: id_info[x][0], reverse=True)
    c_rank = sorted(id_info.keys(), key=lambda x: id_info[x][1], reverse=True)
    e_rank = sorted(id_info.keys(), key=lambda x: id_info[x][2], reverse=True)
    m_rank = sorted(id_info.keys(), key=lambda x: id_info[x][3], reverse=True)
    
    for i, rank_l in enumerate((a_rank, c_rank, e_rank, m_rank)):
        last_grades = -1
        last_rank = 0
        for j, id_ in enumerate(rank_l):
            if id_info[id_][i] != last_grades:
                id_ranks[id_][i] = j + 1
                last_rank = j + 1
            else:                    # 同分同名
                id_ranks[id_][i] = last_rank
            last_grades = id_info[id_][i]
    
    subject_l = ['A', 'C', 'M', 'E']
    for _ in range(M):
        id_ = int(input())
        if id_ in id_ranks:
            best_rank = min(id_ranks[id_])
            best_subject = subject_l[id_ranks[id_].index(best_rank)]
            print(best_rank, best_subject)
        else:
            print("N/A")