N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

class Heap():
    def __init__(self):
        self.l = [1000000 for _ in range(N+1)]
        self.size = 0
    
    def find_mc(self, i):
        if 2*i+1 > self.size:
            return 2*i
        else:
            return max(2*i, 2*i+1, key=lambda x: self.l[x])
    
    def up(self, i):
        while self.l[i//2] < self.l[i]:
            self.l[i//2], self.l[i] = self.l[i], self.l[i//2]
            i //= 2
    
    def down(self, i):
        while i <= self.size//2:
            mc = self.find_mc(i)
            if self.l[mc] > self.l[i]:
                self.l[mc], self.l[i] = self.l[i], self.l[mc]
            else:
                break
            i = mc
    
    def pop(self):
        self.l[1], self.l[self.size] = self.l[self.size], self.l[1]
        self.size -= 1
        self.down(1)
    
    def heapiry(self, ul):
        self.l = [1000000] + ul
        self.size = len(ul)
        for i in range(self.size//2, 0, -1):
            self.down(i)
    
if __name__ == "__main__":
    tl = []
    for i in range(2, N):
        tl = list(sorted(a[:i])) + a[i:]
        if tl == b:
            print("Insertion Sort")
            tl = list(sorted(a[:i+1])) + a[i+1:]
            print(' '.join(map(str, tl)))
            exit(0)
    
    my_heap = Heap()
    my_heap.heapiry(a)
    for _ in range(N-1):
        my_heap.pop()
        if my_heap.l[1:] == b:
            print("Heap Sort")
            my_heap.pop()
            print(' '.join(map(str, my_heap.l[1:])))