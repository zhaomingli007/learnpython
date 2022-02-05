class Solution:
    def calculate(self, s: str) -> int:
        """
        3+40*5/20-1 = 22
                  i
                  j
                  ^
  stack:[3,+,10,-,1]
            
        """
        s = s.strip()
        stack = deque()
        n = len(s)
        i,j = 0, 0
        ops = ['+','-','*','/']
        l = len(s)
        for c in range(l+1):
            if c<l and s[c] not in ops:
                j+=1
            else:
                d = s[i:j]
                if stack and stack[-1] in ['*','/']:
                    op = stack.pop()
                    stack[-1] = int(stack[-1]) * int(d) if op == '*' else int(stack[-1]) // int(d)
                else:
                    stack.append(d)
                j+=1
                i = j
                if c < l:
                    stack.append(s[c])
                    
        v1 = int(stack.popleft())
        while len(stack) > 0:
            op = stack.popleft()
            v2 = stack.popleft()
            v1  = v1+int(v2) if op == '+' else v1 - int(v2)
            
        return v1