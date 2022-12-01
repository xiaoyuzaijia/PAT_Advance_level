N = int(input())
info = {}

if __name__ == "__main__":
    for _ in range(N):
        name, id_, g = input().split()
        info[int(g)] = (name, id_)
    
    g1, g2 = map(int, input().split())
    if g1 > g2:
        g1, g2 = g2, g1
    l = [g for g in info.keys() if g1<=g<=g2]
    l.sort(reverse=True)
    
    if not l:
        print("NONE")
        exit(0)
    
    for g in l:
        print(info[g][0], info[g][1])

        
'''
输入的每一行是一个成绩记录,所以可能出现同样的id.
但题目说每个记录分数都不同,所以用分数作为字典的key.
'''