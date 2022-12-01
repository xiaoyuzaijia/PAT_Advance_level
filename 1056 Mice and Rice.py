N, G = map(int, input().split())
rank = [-1 for _ in range(N)]

def play(pl):
    if len(pl) == 1:
        rank[pl[0]] = 1
        return
    
    losel = pl.copy()
    winl = []
    for i in range(0, len(pl), G):
        win = max(pl[i:i+G], key=lambda x: w[x])
        winl.append(win)
        losel.remove(win)
    
    for i in losel:
        rank[i] = len(winl) + 1
    
    play(winl)

if __name__ == "__main__":
    w = list(map(int, input().split()))
    pl = list(map(int, input().split()))
    
    play(pl)
    
    print(' '.join(map(str, rank)))