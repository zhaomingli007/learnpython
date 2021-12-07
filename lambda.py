add10 = lambda x: x+10

print(add10(10))

mult = lambda x, y:x*y

a = [(1,2), (15,1),(5,-1),(10,4)]
sort_a = sorted(a, key=lambda x:x[1])
print(sort_a)

l1 = [1,2,3,4,5]
l2 = map(lambda x:x+2, l1)
print(list(l2))

l3 = [x+2 for x in l1]
print(l3)

l4 = filter(lambda x:x%2==0, l1)
print(list(l4))

l5 = [x%2==0 for x in l1]
print(l5)
l6 = [x for x in l1 if x%2==0]
print(l6)

from functools import reduce
prod = reduce(lambda x,acc:x*acc, l1)
print(prod)