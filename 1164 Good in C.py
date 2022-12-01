d = dict(zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [[] for _ in range(26)]))

def print_word(w):
    for i in range(7):
        print_l = []
        for j in w:
            print_l.append(d[j][i])
        print(' '.join(print_l))

if __name__ == "__main__":
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for j in range(7):
            d[i].append(input())
    
    input_s = input()
    words = ''.join(map(lambda x: ' ' if x not in d.keys() else x, input_s)).split()

    for i in words[:-1]:
        print_word(i)
        print()
    print_word(words[-1])