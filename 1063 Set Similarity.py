N = int(input())
sets = []

def simil(s1, s2):
    return len(s1 & s2) / len(s1 | s2)

if __name__ == "__main__":
    for _ in range(N):
        s = set(map(int, input().split()[1:]))
        sets.append(s)
    
    k = int(input())
    for _ in range(k):
        s1, s2 = map(int, input().split())
        sim = simil(sets[s1-1], sets[s2-1])
        print(f"{sim:.1%}")