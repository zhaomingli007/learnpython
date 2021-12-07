
def formnum(n, lookup={}):
    if n<0:
        return 0
    if n==0:
        return 1
    if n not in lookup:
        lookup[n] = formnum(n-1)+formnum(n-3)+formnum(n-5)
    return lookup[n]
print(formnum(40))