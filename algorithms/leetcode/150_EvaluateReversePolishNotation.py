class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        
        """
        s = []
        ops = ['+', '-', '*', '/']
        for c in tokens:
            if c in ops:

                v1, v2 = int(s.pop()), int(s.pop())
                sign = 1 if v1 * v2 > 0 else -1
                # print(v2,c,v1, sign)
                if c == '+':
                    s.append(v1+v2)
                elif c == '-':
                    s.append(v2-v1)
                elif c == '*':
                    s.append(v1*v2)
                else:
                    s.append(sign * (abs(v2) // abs(v1)))
            else:
                s.append(c)
            # print(s)
        return s.pop()
