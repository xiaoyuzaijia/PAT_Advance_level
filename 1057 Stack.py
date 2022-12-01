N = int(input())

class Stack():
    def __init__(self):
        self.s = []
    
    def is_empty(self):
        if not self.s:
            return True
        else:
            return False
    
    def push(self, key):
        self.s.append(key)
    
    def pop(self):
        if not self.is_empty():
            return self.s.pop()
        else:
            return "Invalid"
    
    def peek_median(self):
        if not self.is_empty():
            l = list(sorted(self.s))
            return l[(len(l)+1)//2-1]
        else:
            return "Invalid"
    
if __name__ == "__main__":
    my_s = Stack()
    for _ in range(N):
        input_l = input().split()
        if input_l[0] == "Push":
            my_s.push(int(input_l[1]))
        elif input_l[0] == "Pop":
            print(my_s.pop())
        elif input_l[0] == "PeekMedian":
            print(my_s.peek_median())


'''
3个测试点超时...
'''