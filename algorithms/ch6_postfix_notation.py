
def evaluate(v1, v2, op):
    d1, d2 = int(v1), int(v2)
    if op == '+':
        return d1 + d2
    elif op == '-':
        return d2 - d1
    elif op == '*':
        return d2 * d1
    elif op == '/':
        return d2 / d1

def postfix_notation(notatation):
    if not notatation or len(notatation) == 0:
        return None
    ops = set('+-*/')
    vector = list(notatation)
    stack = []
    for c in vector:
        if c in ops:
            if len(stack)<2:
                raise ValueError('invalid postfix expresssion')
            v1 = stack.pop()
            v2 = stack.pop()
            res = evaluate(v1, v2, c)
            stack.append(res)
        else:
            stack.append(c)
    return stack[0] 

if __name__ == '__main__':
    t = postfix_notation('4572+-*')
    print(t)
    t2 = postfix_notation('34+2*7/')
    print(t2)
    
