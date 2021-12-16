from sys import maxsize
class MinStack(object):
    """ Use a stack with tuple entry"""
    
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append((x, min(self.getMin(), x)))
        
    def pop(self):
        self.stack.pop()
        
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1][0]

    def getMin(self):
        if len(self.stack) > 0:
            return self.stack[-1][-1]
        return maxsize

if __name__ == '__main__':
    stk = MinStack()
    stk.push(1)
    stk.push(8)
    stk.push(-7)
    print(stk.getMin())
    stk.pop()
    print(stk.getMin())
    
